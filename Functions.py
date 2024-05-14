import json
import shutil
import os
import re
from msvcrt import getch
from colorama import Fore
def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))

def Head():
    Text = """
                                        (===========================)
                                       (          MY CONTACT         )
                                        (===========================)
"""
    print_centre(Text)

def Option():
    op = """
[01] Add Contact
[02] Search Contact
[03] Update Contact
[04] Show Contact
[05] Delete Contact
[06] Show All Contact
[00] Exit """
    print_centre(op)


def save_contacts(contacts):
    with open("contacts.json", "w") as json_file:
        json.dump(contacts, json_file, indent=4)


def Show_All_Contact(contacts):
    count = 1
    print(Fore.YELLOW+"*-------------------------------------------*"+Fore.RESET)
    for contact in contacts:
            data =  contacts[contact]
            show = f"""    The Contact number {count}
    Name    : {data['name']}                       
    Number  : {data['number']}                         
    Email   : {data['email']}           
    Address : {data['address']}
{Fore.YELLOW}*-------------------------------------------*{Fore.RESET}"""
            print(show)
            count+=1
    print("\nPress Any Key to Continue...")
    getch()
    os.system("cls")
    Head()
    Option()
    
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
def is_valid_phone_number(number):
    pattern = r'^\+?\d{1,3}[- ]?\d{3}[- ]?\d{3}[- ]?\d{4}$'
    return re.match(pattern, number) is not None
def Update_Contact(contacts):
        name = input("Enter the name of the contact to update: ")
        name = name.lower()
        if name in contacts:
            while True:
                number = input("Enter New Phone Number : ")
                number = number.lower()
                if not is_valid_phone_number(number):
                    Note_Red("Please Enter Valid Phone Number!")
                else:
                    break
            while True:
                email = input("Enter New Email : ")
                email = email.lower()
                if not is_valid_email(email):
                    Note_Red("Please Enter Valid Email!")
                else:
                    break
            address = input("Enter New Address : ")
            address = address.lower()
            if number:
                contacts[name]["number"] = number
            if email:
                contacts[name]["email"] = email
            if address:
                contacts[name]["address"] = address
            save_contacts(contacts)
            print(Fore.GREEN+"Contact updated successfully."+Fore.RESET)
            print("\nPress Any Key to Continue...")
            getch()
            os.system("cls")
            Head()
            Option()
        else:
            print(Fore.RED+"Contact not found."+Fore.RESET)

def Get_Data(a,contacts):
        try:
            if a in contacts:
                return contacts[a]   
            else:
                return "No"
        except Exception as e:
            return "No"

def json_process_input():
        data_list = []
        file = "contacts.json"
        with open(file) as qn:
            data = json.load(qn)
            for i in data:
                data_list.append(data[i])

            return data_list
                
def MyFunc(value):
    return (value // 4) * 4

def json_process(out):
    Data =  json_process_input()
    data_list = []
    for i in range(len(Data)):
        x = Data[i]
        data_list.append(x['name'])
        data_list.append(x['number'])
        data_list.append(x['email'])
        data_list.append(x['address'])
        
    name_list = []
    for k in range(len(data_list)):
        t = data_list[k]
        txt = t.lower()
        x = txt.split() 
        y = out.split()
        
        for i in range(len(x)):
            for j in range(len(y)):
                if x[i] == y[j]: 
                    name_list.append(txt)
        continue
    return name_list

def Searching_Contact(value):
    Data =  json_process_input()
    data_list = []
    for i in range(len(Data)):
        x = Data[i]
        data_list.append(x['name'])
        data_list.append(x['number'])
        data_list.append(x['email'])
        data_list.append(x['address'])
    match_index = []
    for j in range(len(data_list)):
        if data_list[j] == value:
            match_index.append(j)
            continue
    name_list = []
    for y in range(len(match_index)):
        ix = MyFunc(match_index[y])
        name_list.append(data_list[ix])
    return name_list
def Note_Green(a):
    note = Fore.YELLOW+ "Note => " + Fore.RESET + Fore.GREEN + a + Fore.RESET
    print(note)
def Note_Red(a):
    note = Fore.YELLOW+ "Note => " + Fore.RESET + Fore.RED + a + Fore.RESET
    print(note)
def add_contact(contacts):
    Note_Red("Remember That You Will Not Able To Change Only Your Contact Name Next Time")
    name = input("Enter name : ")
    name = name.lower()
    while True:
        number = input("Enter New Phone Number : ")
        number = number.lower()
        if not is_valid_phone_number(number):
            Note_Red("Please Enter Valid Phone Number!")
        else:
            break
    while True:
        email = input("Enter New Email : ")
        email = email.lower()
        if not is_valid_email(email):
            Note_Red("Please Enter Valid Email!")
        else:
            break
    address = input("Enter Address : ")
    address = address.lower()
    data = {
        name: {
            "name": name,
            "number": number,
            "email": email,
            "address": address
        }
    }
    try:
        if type(contacts[name]) != "":
                return "sorry"
        else:
               return data
    except Exception as e:
            return data


def Delete_contact(contacts):
    while True:
        Note_Red("It will Delete Your Contact Permanently")
        name = input("Enter the name for delete Contact (If No type N): ")
        if name == 'N' or name == 'n':
             break
        elif name in contacts:
            del contacts[name]
            save_contacts(contacts)
            print(Fore.GREEN+"Contact Deleted successfully."+Fore.RESET)
            print("Press Any Key to Continue...")
            getch()
            os.system("cls")
            Head()
            Option()
            break
        else:
            print(Fore.RED+"Contact not found."+Fore.RESET)