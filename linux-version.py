import pickle as pk
import os
class dns:
    def __init__(self , name , ip) -> None:
        self.name = name 
        self.ip = ip
    def save(self):
        with open(f"dns-servers/{self.name}" , "wb") as f :
            pk.dump(self , f)
        
    def remove(self):
        os.remove(self.name)
    
    def write(self):
        with open("/etc/resolv.conf" , "w") as file :
            file.write(f'\nnameserver {self.ip}')
        
a = dns("nem" , "1234")
a.save()