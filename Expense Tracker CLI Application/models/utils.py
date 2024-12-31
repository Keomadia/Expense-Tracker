# with  the expenses part of the persons database if they decide to export csv file the info from there will be used to create a file
import json
import random
from datetime import datetime
import os
import csv 


THIS_FILE_PATH = os.path.abspath(__file__)
ABS_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(ABS_PATH)
FP = os.path.join(ABS_PATH,'database.json')



def load_db():
    with open(FP,'r') as file:
        data = json.load(file)
    return data

def save_to_db(input):
    has_saved = False
    with open (FP,'w') as db:
        json.dump(input,db,indent=4)
        has_saved = True
    return has_saved

def generate_new_id(fname,lname):
    num = random.randrange(11,99)
    new_id = fname[0:3].capitalize() + str(num) + lname[-1].upper()
    return str(new_id)

def signup(fname,lname,password):
    sign = "Unsuccessful"
    db = load_db()
    if len(db) > 0:
        new_id = generate_new_id(fname,lname)
        if new_id in db:
            print("Id exists")
        else:
            details =   {new_id:{"firstname":fname , "lastname":lname ,"fullname": fname+" " + lname,"password":password,"expenses":{"Food":[],"Entertainment":[],"Transport":[],"Health":[],"Miscellanous":[],"Others":[]}}}
            db.update(details)
            if save_to_db(db):
                sign = True
            else:
                sign = "Couldn't complete the request"   
    else:
        new_id = generate_new_id(fname,lname)
        details =   {new_id:{"firstname":fname , "lastname":lname ,"fullname": fname +" "+ lname,"password":password,"expenses":{"Food":[],"Entertainment":[],"Transport":[],"Health":[],"Miscellanous":[],"Others":[]}}}
        db.update(details)
        if save_to_db(db):
            sign = True
        else:   
            sign = "Couldn't complete the request"
    return sign,new_id

def generate_options_signup():
    options  = ["Sign up","Log in","Exit"]
    for i,j in enumerate(options,1):
        print(i,j)

def login(username,password):
    logged_in = "Unsuccessful"
    data_b = load_db()
    if username in data_b:
        for user in data_b:
            if user == username:
                if data_b[user]["password"] == password:
                    logged_in  = "Successful"
                else:
                    logged_in = "Invalid Password"
    else:
        logged_in = "User does not exist try Again"
    return logged_in

def get_name(username):
    db = load_db()
    for users in db:
        if users == username:
            return db[users]["fullname"]
        
def change_id():
    print("Id can't be changed")
   
def get_categories(username):
    data = load_db()
    for user in data:
        if username == user:
            print("Expenses")
            for stuffs in data[user]['expenses']:
                for expenses in stuffs:
                    print(expenses , end=" ,")             

def generate_options_login():
    print("Pick an Option...")
    options = ["Add an Expense","Export Expenses","See all Expenses","Total Expense","Delete a Category","Add new Category","Log out"]
    for i,j in enumerate(options,1):
        print(i,j)

def user_categories(username):
    data = load_db()
    for user in data:
        if username == user:
            lst = []
            for stuffs in data[user]['expenses']:
                lst.append(stuffs)
            lst = tuple(lst)
            print(lst)
    return lst
  
def add_expense(username,amount,category,desc,date=datetime.now().strftime("%d %b %Y"),):
    done = False
    data = load_db()
    for dat in data:
        if username == dat:
            for vals in data[dat]["expenses"]:
                expenses = data[dat]["expenses"]
                if category == vals:
                    expenses[vals].append(
                             { "date": date,
                                "desc":  desc,
                                "amount": amount
                            
                            }
                        )
                    save_to_db(data)
                    done = True
    return done                          
  
def add_new_category(username,category):
    existing = user_categories(username)
    if category in existing:
        done = f"{category} Already Exists"
    else:
        data = load_db()
        for user in data:
            if user == username:
                category = category.capitalize()
                for j in data[user]:
                    if j == "expenses":
                        data[user][j].update({category:[]})
                        save_to_db(data)
            done = True
    return done         
  
def get_total_expense(username):
    data_b = load_db()
    for user in data_b:
        if user == username:
            llst = []
            expenses = data_b[user]["expenses"]
            for cate in expenses:
                for b in expenses[cate]:
                    x = b['amount']
                    llst.append(x)
    total = sum(llst)
    return total


def get_item_total_expense(category,username):
    data = load_db()
    if not category in user_categories(username):
        return "Invalid Category"        
    else:
        for user in data:
            if user == username:
                llst = []
                expenses = data[user]["expenses"]
                for categories in expenses:
                    category = category.capitalize()
                    if category == categories:
                        if expenses[categories] != []:
                            for i in expenses[categories]:
                                llst.append(i["amount"])
                        else:
                            llst.append(0)

    total = sum(llst)
    return total

def get_all_expenses(username):
    dat_b = load_db()
    print("Here's a list of all your Expenses")
    for user in dat_b:
        if user ==  username:
            expenses = dat_b[user]['expenses']
            for category in expenses:
                print(f"{category}")
                if expenses[category] != []:
                    for i in expenses[category]:
                        print(f"    On {i['date']},You spent ₦{i['amount']:,}{'':4} description - {(i['desc'])}")
                else:
                    continue


def del_category(username,category):
    category = category.capitalize()
    existing = user_categories(username)
    if category in existing:
        print(category,"Exists")
        data = load_db()
        for user in data:
            if user == username:
                expenses = data[user]["expenses"]
                for key,value in expenses.items():
                    if key == category: 
                        expenses.pop(key)
                        save_to_db(data)
                        done = True
                        break
    else:
        done = f'The Category "{category}" Does not Exist'
    return done
      
    
def export_csv(username,filename):    
    Successful = False
    if filename == "":
        filename = "export"
    else:
        filename = filename.replace(' ','_')
        
        
    CSVFP = os.path.join(PROJECT_DIR,f'{filename.capitalize()}.csv')
    with open(CSVFP , 'w',newline='') as file:
        db = load_db()
        writer = csv.DictWriter(file , fieldnames=["date","description","amount","category"])
        writer.writeheader()
        for user in db:
            if user == username:
                expenses = db[user]['expenses']
                for category in expenses:
                    for vals in expenses[category]:
                        writer.writerow({"date": vals['date'],"description": vals['desc'],"amount":vals['amount'],"category": category})
                    Successful = True
    return Successful , CSVFP