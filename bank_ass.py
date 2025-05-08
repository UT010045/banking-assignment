
import sys
import os

def get_customer_info():
  name=input("enter your name:")
  address=input("enter your address:")
  username=input("enter the username:")
  password=input("enter your password:")

  return [name,address,username,password]

def create_customer_next_id():
    if os.path.exists("customers.txt"):
        with open("customers.txt","r") as customer_file:
            lines = customer_file.readline()
            if not lines: 
                return"U001"
            last_line = lines[-1].strip()
            last_id = last_line.split(",")[0]
            next_id_num = int(last_id[1:]) + 1
            return f"U{next_id_num:03}"
    return"U001"

def create_customer():
    customer = get_customer_info()
    with open("customer.txt","w") as file:
        file.write(f"{customer[0]},{customer[1]}\n")

def create_user():
    user = get_customer_info()
    with open("user.txt","w") as file:
        file.write(f"{customer[2]},{customer[3]}")

def view_all_customer():
    with open("customers.txt","r") as file:
        for customer in customer_file . readline():
            print("customer")

accounts={}
account_number= 000

def create_account():
    global account_number
    name= input("enter account user name:")
    try:
        initial_balance=float(input("enter initial balance"))
        if initial_balance < 0:
            print("initial balance cannot ve nagative:")
            return
    except ValueError:
        print ("invaild input.please enter vaild input")
        return
    
    acc_num = account_number
    accounts[acc_num] = {
        "name" : name,
        "balance" : initial_balance,
        "transactions" : [("Initial Deposit" , initial_balance)] 
    }
    account_number += 1
    print(f"account created successfull! Account Number = {account_number}")


def deposit_money():
    acc_no = int(input("enter account number"))
    if acc_no not in accounts:
        print("Account not found")
        return
    amount =float (input(":enter the deposit amount"))
    if amount <= 0:
        print("amount is positive")
        return
    if amount>accounts[acc_no]["balance"]:
        print ("insuffucient balance")
        return
    accounts[acc_no]["balance"] += amount
    accounts[acc_no]["transaction"].append(("deposit",amount))
    print ("deposit successfull!")

def withdraw_money():
    acc_no = int(input("enter account number"))
    if acc_no not in accounts:
        print("Account not found")
        return
    amount = float(input("enter the withdraw amount"))
    if amount <= 0:
        print("amount is positive")
        return
    if amount>accounts[acc_no]["balance"]:
        print ("insuffucient balance")
        return
    accounts[acc_no]["balance"] += amount
    accounts[acc_no]["transaction"].append(("withdraw",amount))
    print ("withdraw successfull!")


def check_balance():
    try: 
        acc_no=int(input("enter your account number"))
        if acc_no not in accounts:
            print("account is not found")
            return
        print(f"current balance is {accounts[acc_no]["balance"]}")
    except ValueError:
        print ("invaild input")

def transaction_history():
    try: 
        acc_no=int(input("enter your account number"))
        if acc_no not in accounts:
            print("account is not found")
            return
        print(f"transaction history for account{acc_no}:")
    except ValueError:
        print ("invaild input")

        
def main():
    while True:
        print("1.Create account\n")
        print("2.Deposit money\n")
        print("3.Withdraw money\n")
        print("4.Check balance\n")
        print("5.Transaction history\n")
        print("6.Exit\n")

        choice=(input("enter your choice(1-6):"))
        if choice=="1":
          create_account()
        elif choice=="2":
          deposit_money()
        elif choice=="3":
          withdraw_money()
        elif choice=="4":
          check_balance()
        elif choice=="5":
          transaction_history()
        elif choice=="6":
          print("Thanks you for using")
        break
main()

 









    












  
