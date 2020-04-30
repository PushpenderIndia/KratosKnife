import base64

class Encrypt:
    def __init__(self):
        self.text = ""
        self.enc_txt = ""

    def encrypt(self, filename):
        
        with open(filename, "r", encoding="utf8") as f:
            lines_list = f.readlines()
            for lines in lines_list:
                self.text += lines
              
            self.text = self.text.encode()
            self.enc_txt =  base64.b64encode(self.text)   

        with open(filename, "w") as f:
            f.write(f"import base64; exec(base64.b64decode({self.enc_txt}))")
            
    
if __name__ == '__main__':   
    filename = input("[?] Enter Filename : ")
    
    print(f"\n[*] Initaiting Base64 Encryption Process ...")    
    test = Encrypt()
    test.encrypt(filename)
    print(f"[+] Operation Completed Successfully!\n")