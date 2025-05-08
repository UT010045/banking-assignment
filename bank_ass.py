def get_customer_info():
  name=input("enter your name:")
  address=input("enter your address:")
  username=input("enter the username:")
  password=input("enter your password:")

  return=[name,address,username,password]

def create_customer_next_id():



choice=int(input("enter your choice(1-6):"))
if choice=="1":

    customer_user_name=input("enter your name:")
    customer_password=input("enter the password:")
    customer_id_number=input("enter the aid number:")

    file =open("user details.txt","a")
    file.write(f"Name: {customer_user_name}\n")
    file.write(f"password: {customer_password}\n")
    file.write(f"id_number: {customer_account_number}\n")
    file.close()

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
    account_no = int(input("enter account number"))
    if account_no not in accounts:
        print("Account not found")
        return
    amount = float(input("enter the withdraw amount"))
    if amount <= 0:
        print("amount is positive")
        return
    if amount>accounts[account_no]["balance"]:
        print ("insuffucient balance")
        return
    accounts[account_no]["balance"] += amount
    accounts[account_no]["transaction"].append(("withdraw",amount))
    print ("withdraw successfull!")


def deposit_money():
    account_no = int(input("enter account number"))
    if account_no not in accounts:
        print("Account not found")
        return
    amount =float (input(":enter the deposit amount"))
    if amount <= 0:
        print("amount is positive")
        return
    if amount>accounts[account_no]["balance"]:
        print ("insuffucient balance")
        return
    accounts[account_no]["balance"] += amount
    accounts[account_no]["transaction"].append(("deposit",amount))
    print ("deposit successfull!")


def check_balance():
    try: 
        account_no=int(input("enter your account number"))
        if account_no not in accounts:
            print("account is not found")
            return
        print(f"current balance is {accounts[account_no]["balance"]}")


def transaction_history():
    try: 
        account_no=int(input("enter your account number"))
        if account_no not in accounts:
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






    












  
