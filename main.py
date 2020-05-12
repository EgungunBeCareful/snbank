#-*-coding:utf8;-*-
#qpy:

import pickle
import os
import pathlib

def getDetails():
    with open('staff.txt') as file:
        staff_details = file.readlines() 
        file.close() 
        return staff_details

def saveSession(user_name, user_pwd):
    with open("temp.txt", "w", encoding='utf-8') as file:
         file.write('{}\n'.format(user_name)) 
         file.write('{}\n'.format(user_pwd)) 
         session = [user_name, user_pwd] 
         return session
         
def saveAccount(customer_details):
    with open('customer.txt', 'w') as file:
        for item in customer_details:
            file.write("{}\n".format(item))
        
def displayDetails(acctNo):
    with open('customer.txt', 'w+') as f:
        read_data = f.readlines()
        f.close()
        if(acctno == read_data[4].strip('\n')):
            return read_data 
            
def confirmFile(file):
    if os.path.exists(file): 
    return True 
    
def deleteSession(filename):
    if os.path.exists(filename): 
    os.remove(filename)   
      

def appOptions(session):
    try:
        print("1. Create new bank account \n2. Check Account Details \n3. Logout ")
        staff_option = int(input("Please choose option 1 or 2 or 3? ")) 
        if(staff_option == 1):
            #get user account details for creating account 
            accName = input("Enter Customer's full name: ") 
            deposit = input("Enter opening deposit: ") 
            accType = input("Enter Chosen Account type C/S:") 
            accEmail = input("Please provide Email Address:") 
            accNumber = random.randint(1000000000,9999999999) #generate random 10 numbers
            print(f'Your new account number is: {accNumber}')
           
            customer_details = [accName, deposit, accType, accEmail, accNumber]
             
             # Save information in customers file 
            saveAccount(customer_details) 
            appOptions(session) 
             
         elif(staff_option == 2):
             while(confirmFile('temp.txt')):
                 inputAccNo = input("Please provide Account Number: ")
                 print("The account details are as follows: ")
                 returnDetails = displayDetails(inputAccNo) 
                 print(f"{customer_details}") 
                 appOptions(session)
         elif(staff_option == 3):
             print("*******Logging out*****") 
             
             #delete user session
             deleteSession('temp.txt')
         else: print(" Try again")
     except ValueError:
         print("******Please Enter a valid number******") 

def appRegister():
    if not os.path.exists('staff.txt'):
        file = open('staff.txt', 'w')
        file.close() 
        username = input('Enter username: ')
        if username in open('staff.txt', 'r').read():
            print('Username already exists') 
            exit() 
            password = input('Enter password: ')
            c_password = input('Enter confirm password: ') 
            if password != c_password:
                print('Sorry password do not match') 
                exit()
                handle = open('staff.txt', 'a') 
                handle.write(username) 
                handle.write(' ') 
                handle.write(password) 
                handle.write('\n') 
                handle.close() 
                print('User was successfully registered')
                exit()

def appLogin():
    {1:'Login', 2:'Close App'} 
    while True:
        try:
            print("1. Login \n2. Close App")
            user_choice = int(input("Please choose option 1 or 2? "))
            if(user_choice == 1):
                username1 = input("USERNAME: ")
                password1 = input("PASSWORD: ")
                for row in file:
                    field = row.split(",") 
                    username = field[0]
                    password = field[1]
                    lastchar = len(password)-1 
                    password = password[0:lastchar]
                    if username1 == username and password1 == password:
                        print("Hello",username)
                        break 
                    else:
                        print("incorrect")
                         
                 print("Login successful, Welcome, (user_name1)") 
            else:
                 print("------------Please Try again---------------\nYour credentials do not match any record") 
       elif(options == 2):
           print("Good bye! Thank you for using Bank Management System")
           break 
       else:
           print("Please Try again") 
       except ValueError:
           print("******Please Enter a valid number******")

user = input("Are you already a registered user? yes/no") 
if user == "yes":
    appLogin() 
elif user =="no":
    appRegister() 

print("Welcome to SN Bank")
