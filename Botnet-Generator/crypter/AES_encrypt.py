from Crypto import Random
from Crypto.Cipher import AES
import os
import hashlib

class Encryptor:
    def __init__(self, key, file_name):
        self.plainkey = key
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.file_name = file_name

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)
        
    def encrypt_file(self):
        with open(self.file_name, 'rb') as f:
            plaintext = f.read()
        enc = self.encrypt(plaintext, self.key)
        with open(self.file_name, 'w') as f:
            f.write("from Crypto import Random\n")
            f.write("from Crypto.Cipher import AES\n")
            f.write("import hashlib\n")
            
            f.write("\nclass Decryptor:\n")
            f.write("\tdef __init__(self, key, file_name):\n")
            f.write("\t\tself.key = hashlib.sha256(key.encode('utf-8')).digest()\n")
            f.write("\t\tself.file_name = file_name\n\n")
            
            f.write("\tdef pad(self, s):\n")
            f.write("\t\treturn s + b\"\\0\" * (AES.block_size - len(s) % AES.block_size)\n\n")
            
            f.write("\tdef decrypt(self, ciphertext, key):\n")
            f.write("\t\tiv = ciphertext[:AES.block_size]\n")
            f.write("\t\tcipher = AES.new(key, AES.MODE_CBC, iv)\n")
            f.write("\t\tplaintext = cipher.decrypt(ciphertext[AES.block_size:])\n")
            f.write("\t\treturn plaintext.rstrip(b\"\\0\")\n\n")
            
            f.write("\tdef decrypt_file(self):\n")
            f.write("\t\tdec = self.decrypt(self.file_name, self.key)\n")
            f.write("\t\treturn dec\n\n")
            
            f.write("class BruteForce:\n")
            f.write("\tdef __init__(self, encrypted_codes):\n")
            f.write("\t\tself.encrypted_codes = encrypted_codes\n")
            f.write("\t\tself.password = 0\n\n")
            
            f.write("\tdef start(self): \n")
            f.write("\t\tstatus = True\n")
            f.write("\t\twhile status:\n")
            f.write("\t\t\ttry:\n")
            f.write("\t\t\t\tprint(f\"\\rPassword : {self.password}\", end=\"\")\n")       #Comment This Line      
            f.write("\t\t\t\ttest = Decryptor(str(self.password), self.encrypted_codes)\n")
            f.write("\t\t\t\tdecrypted_code = test.decrypt_file()\n")
            f.write("\t\t\t\texecutable = decrypted_code.decode() \n")
            f.write("\t\t\t\tstatus = False\n")
            f.write("\t\t\t\treturn executable \n")
            f.write("\t\t\texcept UnicodeDecodeError:\n")
            f.write("\t\t\t\tself.password += 1\n\n")
            
            f.write(f"encrypted_codes = {enc}\n")
            f.write(f"brute = BruteForce(encrypted_codes)\n")
            f.write(f"executable = brute.start()\n")
            f.write("exec(executable)\n")      


if __name__ == '__main__':
    notice = """
    Cracking Speed on RunTime
    =========================
    With 2 GB RAM & 1 GHz Proceessor 
    --------------------------------    
    Guess Speed: 2000 Numeric Pass/ Seconds

    Password Like : 10000 is cracked in 5 seconds
    So Delay Time In Program Will be 5 seconds
    
    """
    print(notice)

    key = input("[?] Enter Numeric Key : ")
    path = input("[?] Enter Path of File : ")

    print("\n[*] Initiating Encryption Process ...")
    test = Encryptor(key, path) 
    test.encrypt_file()
    print("[+] Process Completed Successfully!")
