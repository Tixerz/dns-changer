import pickle as pk
import os
class dns:
    def __init__(self , name , ip) -> None:
        self.name = name 
        self.ip = ip
    def save(self):
        with open(f"dns-servers/{self.name}" , "wb") as f :
            pk.dump(self , f)
        
    def write(self):
        with open("/etc/resolv.conf" , "a") as file :
            file.write(f'\nnameserver {self.ip}')

def add_server():
    os.system("clear")
    name=input("--------------------\nEnter the name of the server: ")
    
    ip = input("--------------------\nEnter the ip address: ")
    obj = dns(name, ip)
    obj.save()
    
    obj_list = []
    for item in os.listdir("dns-servers/") :
        with open(f"dns-servers/{item}" , 'rb') as file:
            obj_list.append(pk.load(file))
    main_menu()
obj_list = []
for item in os.listdir("dns-servers/"):
    with open(f"dns-servers/{item}" , 'rb') as file :
        obj_list.append(pk.load(file))
    
def show_servers():
    global obj_list
    os.system("clear")
    print("0- <Back>")
    counter = 0
    for item in obj_list :
   
        counter += 1
        print(f"{counter}- {item.name}:     {item.ip}")
    opt = int(input("[choose your option]"))
    if opt == 0 :
        main_menu()
    if opt != 0 :
        obj_list[opt-1].write()
        main_menu()
    
    

def main_menu():
    global user_opt
    os.system("clear")
    print("---------------\n|  Main Menu  |\n---------------")
    print("1- <SERVER LIST>")
    print("2- <ADD SERVER>")

    print("3- <EXIT>")
    user_opt = int(input("[choose your option]"))
    if user_opt ==1 :
        show_servers()
        
    elif user_opt == 2 :
        add_server()
    
       
    
main_menu()
