from models.utils import *

while True:
    print("************************************************************************************************************************")
    generate_options_signup()
    choice = input("Select an Option: \n")
    if choice == '1':
        print("************************************************************************************************************************")
        print("Ready to Create an Account")
        fname = input("Enter Your First Name:")
        lname = input("Your Last name: ")
        password = input("Enter your Password:")
        if fname != ""and lname != "":
            if len(password) > 3:
                sinup,_ = signup(fname,lname,password)
                if sinup:
                    print("Created successfully")
                    print(f"Your username is {_}")
                else:
                    print(sinup)
            else:
                print("Use a stronger password")
        else:
            print("You left some details unfilled")
        
                
    elif choice == '2':
        print("************************************************************************************************************************")
        
        print("Finally you're back\nYour Expenses have been waiting ⌚⌚")
        username = input("Enter Your UserName:")
        password = input("Enter your Password:")
        if username != "":
            log_in = login(username,password)
            if log_in == "Successful":
                print("Logged in successfully")
                print("************************************************************************************************************************")

                print(f"Welcome Back {get_name(username)}")
                while True:
                    print("********************************************************************************************************************")
                    generate_options_login()
                    choix = input("Select an Option: ")
                    if choix == '1':
                        the_other_lst = user_categories(username)
                        print("****************************************************************************************************************")
                        amount = input("Enter Amount: ₦ ")
                        category = input(f"What did you spend ₦ {amount} on ? \n{the_other_lst} : ")
                        desc = input("Write a short description for this expense...")

                        if amount.isdigit():
                            amount = int(amount)
                            another_lst = user_categories(username)
                            if category in another_lst:
                                if add_expense(username,amount,category,desc):
                                    print(f"Successfully Added expense for {category}")
                            else:
                                print(f"The Category {category} was not found")
                                confirmation = input(f"Would you like to go ahead creating a new category {category}? (Y/N)")
                                if confirmation.upper() == "Y":
                                    add_new_category(username,category)
                                    if add_expense(username,amount,category,desc):
                                        print(f"Successfully Added expense for {category}")
                                else:
                                    print("Alright then.....")
                        else:
                            print("Try Again , Invalid AMOUNT")
                    elif choix == "2":
                        if input("Would you like to Export Your Expenses ? Y/N").upper() == 'Y':
                            filename = input("Enter the filename :")
                            Success , the_path = export_csv(username,filename)
                            if Success:
                                print(f"Check in {the_path} for your Csv Document")
                            else:
                                print("Could not Complete Request")
                        else:
                            input("Alright Then \nEnter to Continue\n")
                    
                    elif choix == '3':
                        get_all_expenses(username)
                        print("************************************************************************************************************************")
                        print()
                        input("Press Enter to continue")
                        
                    elif choix == '4':
                        print()
                        print("Do you want \n1. Total Expense\n2. Expense on a particular Category")
                        print("************************************************************************************************************************")
                        choice = input("Enter your choice: ")
                        if  choice == "1":
                            total = get_total_expense(username)
                            print(f"\033[1m{get_name(username)}\033[0m The amount you've spent in total is = ₦{total:,}")
                            input("Press Enter to continue")
                        elif  choice == "2":
                            category = input(f"Pick a category {', '.join(map(str, user_categories(username)))}  :")
                            total = get_item_total_expense(category, username)
                            if isinstance(total,int):
                                print(f"Your total amount spent on {category} is = ₦{total:,}")
                                input("Press Enter to continue")
                            else:
                                print(total)
                                
                    elif choix == '5': 
                        print("Which Category would you like to delete ?")
                        print(', '.join(map(str, user_categories(username))) ,end=" -->")
                        category_for_deletion = input("")
                        if input("Are you sure you want to Delete Y/N ? ").upper() == 'Y':
                            delete = del_category(username,category_for_deletion)
                            if delete == True:
                                print(f"Successfully deleted {category_for_deletion} from Expenses")
                                input("Press Enter to continue")
                            else:
                                print(delete)
                                input("Press Enter to continue")
                        else:
                            print("Alright then ...")
                            input("Press Enter to continue")

                    elif choix == '6': 
                        new_category = input("What would you like to call this category")
                        if input(f"Are you sure you want to Create {new_category} Y/N ? ").upper() == 'Y':
                            if add_new_category(username,new_category) == True:
                                print(f"Successfully added {new_category}")
                            else:
                                print(add_new_category(username,new_category))
                        else:
                            print("Alright then ...")
                            input("Press Enter to continue")
                            
                    elif choix == '7':
                        break
            else:
                print(log_in)
        else:
            print("Invalid Username")
            
    elif choice == '3':
        break
        

