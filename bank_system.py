# Accounting program
# Ask user for login or register
# After the login successfull give him/her choices : 1. view balance 2. add balance 3. redeem balance
# 1. View balance : print the balance of the user by reading the file where balance is stored
# 2. Add balance : read the file where balance is stored and find whether the user has balance or not if there is then add in existing balance if not create a new one
# 3. redeem balance : read the file where balance is stored and find whether the user has balance or not if there is then deduct in existing balance if not print 'you do not have balance'


import json

user_choice = input("Do you want to login or register ? \n\t Login\n\t Register \n\t: ")


def register():
    username = input("\tEnter your user name: ")
    password = input("\tEnter your password : ")

    user_data = {
        "username": username,
        "password": password,
        "balance": 0

        }


    json_data = json.dumps(user_data)

    with open("user_data.txt",'a') as f:
        f.write(json_data+'-')
        print(f"{username.capitalize()} your account create sucessfully!!!")
  


def login():
    username = input("\tEnter your user name: ")
    password = input("\tEnter your password : ")

    with open("user_data.txt",'r') as f:
        user_data = f.read()
        list_user_data= user_data.split('-')
        for i in list_user_data:
             if i != '':
                 dict_data = json.loads(i)
                 if username == dict_data.get('username') and password == dict_data.get('password'):
                   user_login = True
                    

        if user_login == True:
            print(f"\t {username.capitalize()} Login sucessfully !!")
            while True:
                print("-" * 23)
                print(" 1. Add balance")
                print(" 2. View balance")
                print(" 3. Redeem balance")
                print(" 4. Logged out")
                print("-" * 23)
                
                cus_choice = input("Please Enter Your choice: ")
                if cus_choice == '1':
                    add_balance()
                elif cus_choice == '2':
                    view_balance(username)
                elif cus_choice == '3':
                    redeem_balance(username)  
                elif cus_choice == '4':
                    print(f"{username.capitalize()} you are logged out!!")
                    break
        else:
            print("Invalid cerdintals")


def view_balance(username):
    with open("user_data.txt",'r') as f:
         data = f.read()

         user_data= data.split('-')

         for i in user_data:
            if i != '':
   
             dict_data = json.loads(i)
            
             print("Your balance is: ", dict_data.get('balance'))


def add_balance():
    with open("user_data.txt", 'r') as f:
        a= f.read()
        data = a.split('-')
    for i in data:
        if i != '':
            dict_data = json.loads(i)
            print("Your balance is: ", dict_data["balance"])
            print("Enter the amount you want to add: ")
            amount = int(input("Enter the amount: "))
            dict_data["balance"] += amount
            print("Your new balance is: ", dict_data["balance"])
            with open("user_data.txt", "w") as f:
               f.write(json.dumps(dict_data))
           
            

def redeem_balance(username):
    file = open("user_data.txt", "r")
    data = file.read()
    file.close()
    data = data.split('-')
    for i in data:
        if i != '':
            dict_data = json.loads(i)
            print("Your balance is: ", dict_data["balance"])
            print("Enter the amount you want to reedem: ")
            amount = int(input("Enter the amount: "))
            dict_data["balance"] -= amount
            print("Your new balance is: ", dict_data["balance"])
            with open("user_data.txt", "w") as f:
               file.write(json.dumps(dict_data))
           


if user_choice == 'login':
    login()
elif user_choice == 'register':
    register()
while True:
    ask = input("Do you want to restart your app : ")

    if ask == 'yes':
        continue
    elif ask == 'no':
        break
    else:
        print("invalid cerdintals")

    

