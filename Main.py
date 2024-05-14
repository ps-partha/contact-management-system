import os
import Functions
import json
from colorama import Fore
from msvcrt import getch
if __name__ == '__main__':
    os.system("cls")
    Functions.Head()
    Functions.Option()
    try:
        with open("contacts.json", "r") as json_file:
            contacts = json.load(json_file)
    except FileNotFoundError:
        print("File not find!")
    while True:
        quary = input(Fore.CYAN+"\nEnter Option (0-6): "+Fore.RESET)
        if "01" in quary or '1' in quary or "add contact" in quary:
            print("Please Enter Your Contact Information")
            contact = Functions.add_contact(contacts)
            if contact != "sorry":
                contacts.update(contact)
                Functions.save_contacts(contacts)
                print(Fore.GREEN + "Contact Added successfully."+ Fore.RESET)
                print("Press Any Key to Continue...")
                getch()
                os.system("cls")
                Functions.Head()
                Functions.Option()
            else:
                print(Fore.GREEN+"Name Already Exist" + Fore.RED)
        elif "02" in quary or "2" in quary or "search contact" in quary:
            print("Search Your Contact By Any Information (Name Email or Address)")
            while True:
                a = input("Enter search value (If No Type N): ")
                d =  Functions.json_process(a)
                unique_list = []
                for item in d:
                    if item not in unique_list:
                        unique_list.append(item)
                a = a.lower()
                if a == 'N' or a == 'n':
                    break
                else:
                    count = 0
                    for i in range(len(unique_list)):
                        name =  Functions.Searching_Contact(unique_list[i])
                        for i in range(len(name)):
                            Data = Functions.Get_Data(name[i],contacts)
                            if Data != "No":
                                show =Fore.GREEN+ f"""*----------------------------------------------------*
    1. Name    : {Data['name']}                       
    2. Number  : {Data['number']}                         
    3. Email   : {Data['email']}           
    4. Address : {Data['address']}
*----------------------------------------------------*"""+ Fore.RESET
                                count +=1
                                print(show)
                            else:
                                print(Fore.RED+"Contact Not Available"+Fore.RESET)
                    print(Fore.MAGENTA+f"Total {count} Matching Contact Find\n"+Fore.RESET)
                    print("Press Any Key to Continue...")
                    getch()
                    os.system("cls")
                    Functions.Head()
                    Functions.Option()
                    break
        elif "03" in quary or "3" in quary or "update contact" in quary:
            Functions.Note_Green("It will Update Your Contact Information")
            Functions.Update_Contact(contacts)
        elif "04" in quary or "4" in quary or "show contact" in quary:
            print("Showing Contact Information")
            while True:
                user = input("Enter Your Contact Name : ")
                Data = Functions.Get_Data(user,contacts)
                if Data != "No":
                    show =Fore.GREEN+ f"""
*----------------------------------------------------*
            1. Name    : {Data['name']}                       
            2. Number  : {Data['number']}                         
            3. Email   : {Data['email']}           
            4. Address : {Data['address']}                   
*----------------------------------------------------*
                    """+ Fore.RESET
                    print(show)
                    print("Press Any Key to Continue...")
                    getch()
                    os.system("cls")
                    Functions.Head()
                    Functions.Option()
                    break
                else:
                    print(Fore.RED+"Contact Not Available"+Fore.RESET)
                    

        elif "05" in quary or "5" in quary or "delete contact" in quary:
            Functions.Delete_contact(contacts)
        elif "06" in quary or "6" in quary or "show all contact" in quary:
            Functions.Show_All_Contact(contacts)
        elif "00" in quary or "0" in quary or "exit" in quary:
            print("\nThanks For Using This System")
            print("The System Was Exited\n")
            exit()   
        else:
            print("Sorry Enter Valid Option")

