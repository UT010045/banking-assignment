import sys

def get_customer_info():
  name=input("enter your name:")
  address=input("enter your address:")
  username=input("enter the username:")
  password=input("enter your password:")
  return=[name,address,username,password]
get_customer_info()

def create_customer_next_id():
  with open("customers.txt","r") as customer_file:
        print(int(customer_file.readline()[-1].split(",")[0][1:]+1))
      return f"U(int(customer_file.readline()[-1].split(",")[0][1:]+1:03))
create_customer_next_id():

d

accounts={}
account_number=001

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


def check_balance():
    try: 
        acc_no=int(input("enter your account number"))
        if acc_no not in accounts:
            print("account is not found")
            return
        print(f"current balance is {accounts[acc_no]["balance"]}")


def transaction_history():
    try: 
        acc_no=int(input("enter your account number"))
        if acc_no not in accounts:
            print("account is not found")
            return
        






def main():
    while True:
        print("1.Create account\n")
        print("2.Deposit money\n")
        print("3.Withdraw money\n")
        print("4.Check balance\n")
        print("5.Transaction history\n")
        print("6.Exit\n")
        choice=int(input("enter your choice(1-6):"))
        if choice=="1":






    












  
