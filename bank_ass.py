import random
from datetime import datetime

accounts = {}

def login():
    username = input("Enter the username: ")
    password = input("Enter your password: ")

    try:
        with open("login.txt","r") as file:
            for line in file:
                parts = line.strip().split(":")
                if len(parts) == 3:
                    saved_user,saved_pass,role = parts
                    if username == saved_user and password == saved_pass:
                        print (f"login successfull!!")
    except FileNotFoundError:
        print ("Error")

def adminmenu():
    while True:
        print("\n==== Admin Banking Menu ====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Choose your choice (1-6): ")
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            transaction_history()
        elif choice == "6":
            print("Thank you")
            break
        else:
            print("Invalid choice")

def usermenu():
    while True:
        print("\n==== User Banking Menu ====")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Choose your choice (1-5): ")
        if choice == "1":
            deposit_money()
        elif choice == "2":
            withdraw_money()
        elif choice == "3":
            check_balance()
        elif choice == "4":
            transaction_history()
        elif choice == "5":
            print("Thank you")
            break
        else:
            print("Invalid choice")

def create_account():
    name = input("Enter account user name: ")
    user_name = input("Enter login username: ")
    user_password = input("Enter login password: ")
    try:
        initial_balance = float(input("Enter initial balance: "))
        if initial_balance < 0:
            print("Initial balance cannot be negative")
            return
    except ValueError:
        print("Invalid input. Please enter a valid amount")
        return

    account_number = str(random.randint(10000, 99999))
    while account_number in accounts:
        account_number = str(random.randint(10000, 99999))

    accounts[account_number] = {
        "Name": name,
        "balance": initial_balance,
        "transaction": []
    }

    save_account_to_file(account_number, name, user_name, user_password, initial_balance)
    append_login_credentials(user_name, user_password)
    print(f"Account created successfully! Account number: {account_number}")

def save_account_to_file(account_number, name, user_name, user_password, balance):
    with open("create.txt", "a") as file:
        file.write(f"{account_number}:{name}:{user_name}:{user_password}:{balance}\n")

def append_login_credentials(user_name, password, role="user"):
    with open("login.txt", "a") as file:
        file.write(f"{user_name}:{password}:{role}\n")

def deposit_money():
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account not found")
        return
    try:
        amount = float(input("Enter the deposit amount: "))
        if amount <= 0:
            print("Amount must be positive")
            return
    except ValueError:
        print("Invalid amount")
        return

    accounts[account_number]["balance"] += amount
    accounts[account_number]["transaction"].append(("deposit", amount, str(datetime.now())))
    print("Deposit successful!")

def withdraw_money():
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account not found")
        return
    try:
        amount = float(input("Enter the withdrawal amount: "))
        if amount <= 0:
            print("Amount must be positive")
            return
        if amount > accounts[account_number]["balance"]:
            print("Insufficient balance")
            return
    except ValueError:
        print("Invalid amount")
        return

    accounts[account_number]["balance"] -= amount
    accounts[account_number]["transaction"].append(("withdraw", amount, str(datetime.now())))
    print("Withdrawal successful!")

def check_balance():
    account_number = input("Enter your account number: ")
    if account_number not in accounts:
        print("Account not found")
        return
    print(f"Current balance is {accounts[account_number]['balance']}")

def transaction_history():
    account_number = input("Enter your account number: ")
    if account_number not in accounts:
        print("Account not found")
        return
    print(f"Transaction history for account {account_number}:")
    for t in accounts[account_number]["transaction"]:
        print(f"{t[2]} - {t[0]}: {t[1]}")


login()
adminmenu()
usermenu()



 









    












  
