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
        os.remove(f"dns-servers/{self.name}")
        with open("/etc/resolv.conf","r") as f:
            lines=f.readlines()
            print(lines)
        with open("/etc/resolv.conf","w")as f:
            for l in lines:
                if l != f'nameserver {self.ip}':
                    f.write(l)

    
    def write(self):
        with open("/etc/resolv.conf" , "w") as file :
            file.write(f'\nnameserver {self.ip}')
            print(f'\nnameserver {self.ip}')


