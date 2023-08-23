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
a = dns("google dns" , "8.8.8.8")
a.save()
obj_list = []
for item in os.listdir("dns-servers/") :
    with open(f"dns-servers/{item}" , 'rb') as file:
        obj_list.append(pk.load(file))

    
print("---------------------------------------------")
counter = 0
for item in obj_list :
   
    counter += 1
    print(f"{counter}- {item.name}:     {item.ip}")
