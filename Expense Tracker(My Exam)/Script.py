import json
import os

# FP = "C:\\Users\\HP\\Documents\\Me\\My Projects\\Python\\Expense Tracker\\database_two.json"

THIS_FILE_PATH = os.path.abspath(__file__)
ABS_PATH = os.path.dirname(os.path.abspath(__file__))
FP = os.path.join(ABS_PATH,'database_two.json')

def save_to_db(data):
    successful = False
    with open(FP,'w') as file:
        json.dump(data,file,indent=4)
        successful = True
    return successful
    
def verify(name,password):
    Logged_in = False
    for dct in users:
        if name in dct:
            dct = dct
            if dct["password"] == password:
                Logged_in = True
    return Logged_in
                

with open(FP,'r') as file:
    users = json.load(file)

x = 0
welcome = input("Welcome to Octillion Whales EXPENSE TRACKER\nSelect an option to get started\n1. Create Account\n2. Login\n3. Exit\n")
if welcome == '1':
    print("Create your account")
    name = input("Enter your name: ")
    password = input("Set Your Passkey: ")
    confirm_password = input("Confirm Your Passkey: ")
    
    
    if 3 < len(password) < 30:
        if password == confirm_password:
            for dct in users:
                if name in dct:
                    print(f"User Found (Login instead)")
                    input()
            else:
                users.append(
                    {
                        f"{name}":{"Food":[],"Transport":[],"Miscellanous":[],"Health":[],"Subscriptions":[],"Others":[]},
                        "password":f"{password}"
                    }
                    
                )
                
                if save_to_db(users):
                    print("Created Successfully Login man")
                    input()
                else:
                    print("Error")
        else:
            print("Password combination Error")
    
if welcome == '2':
    print("Login to your account")
    login_name = input("Enter your name: ")
    login_password = input("Enter Your Passkey: ")
    if verify(login_name,login_password):
        name = login_name
        print(f"Welcome Back {name}")
        for dct in users:
                if name in dct:
                    expense = dct[name]
        while x == 0:
            reply = input(f"What would you like to do\n1. Add new expense\n2. Update an expense\n3. Delete an Expense\n4. Exit\n")
            if reply == '1':
                name = input("What are you calling this expense ?\n")
                if not name.isdigit() and name != "":
                    expense[f"{name}"] =[]
                    if save_to_db(users):
                        print(f"Successfully added expense {name}\n")
                    else:
                        print("Could not work")
                else:
                    print("That name is not accepted\n")
                    
            elif reply == '2':   # Updating expenses  
                expense_type = input(f"\nWhat type of Expense do you want to track?\nCategory =>{[i for i in expense]} ?")
                if expense_type.isalpha() and expense_type != "":
                    expense_type = expense_type.capitalize()
                    if expense_type in expense:
                        print(f"\nYou selected {expense_type} \n")
                        do = input(f"What do you want to do for {expense_type}\n1. Add Money \n2. Get total expense for {expense_type}\n3. Back")
                        if do == '1':
                            amount = input(f"\nHow much do you want to add for {expense_type}")
                            if amount.isdigit():
                                amount = int(amount)
                                for key,value in expense.items():
                                    if key == expense_type:
                                        value.append(amount)
                                        if save_to_db(users):
                                            print(f"Successfully Added ${amount} for {key}\n")
                                        else:
                                            print("Could not work\n")
                                            
                                            
                        elif do == '2':
                            for key,value in expense.items():
                                if key == expense_type:
                                    print(f"You have spent a total of ${sum(value)} on {expense_type}\n")
                        elif do == '3':
                            print(f"Byeeeee\n")
                        else:
                            print(f"Invalid Selection \ntry again Later\n")
                        
                    else:
                        print(f"\n{expense_type} does not Exist\n")
                        
                else:
                    print("Select from the Category")
                            
            elif reply == '3':   # Deleting an Expense
                expense_type = input(f"Which expense do you want to delete\nCategory =>{[i for i in expense]} ?\n")
                if expense_type.isalpha():
                    expense_type = expense_type.capitalize()
                    if expense_type in expense:
                        print(f"\nYou selected {expense_type}")
                        question = input(f"Are you sure you want to delete {expense_type} Y/N?")
                        if question.isalpha():
                            if question.upper() == "Y":
                                for key,value in expense.items():
                                    if expense_type == key:
                                        if value != []:
                                            value.clear()
                                            print(f"successfully deleted Expense for {expense_type}")
                                            save_to_db(users)
                                        else:
                                            print(f"{expense_type} has no Values in it")
                            else:
                                print("Phew You had me there...\n")
                        else:
                            print("Must be alphabets Try Again Later\n")
                
                
            elif reply == '4':
                print("Bye bye")
                x += 1
            else:
                print("Invalid Selection\n")

    else:
        print("Unsuccessful")
