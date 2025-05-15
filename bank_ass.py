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
        print("2. Check Balance")
        print("3. Transaction History")
        print("4. Transfer money")
        print("5. Password protection")
        print("6. Exit")

        choice = input("Choose your choice (1-6): ")
        if choice == "1":
            Create_account()
        elif choice == "2":
            Check_balance()
        elif choice == "3":
            Transaction_history()
        elif choice == "4":
            Transfer money()
        elif choice == "5":
            Password protection()
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

def Transer Money():
    from_acc= input("Enter your Account Number: ")
    if from_acc not in Account:
        print("Sender Account Number is Wrong.")
        return
    to_acc = input("Enter Recipient Account Number:")
    if to_acc not in Account:
        print("Recipient Account Number is Wrong.")
        return
    try:
       amount float(input("Enter Amount to Transfer: "))
       if amount <= 0:
          print("Amount Must be Greater than 8.")
          return
       if amount > Account[from_acc] ["Balance"]:
          print("Insufficient Balance on Account")
          return

       Account[from_acc]["Balance"] -- amount
       Account[to_acc] ["Balance"] += amount
       Account[from_acc]["Transactions"].append(f"Transferred ${amount:.2f} to {to_acc}")
       Account[to_acc] ["Transactions"].append(f"Transferred $(amount:.2f} to {from_acc}")
       print(f"Transfer Successful.${amount:.2f} transferred from (from_acc) to (to_acc}")
    except ValueError:
       print("Invalid Amount.")

def Change_Password():
    UserNAME = input("Enter Your User Name:")
    Old_Password = input("Ender Your Old Password:")
    
    updated_lines = []
    found = False

    try:
        with open("login.txt", "r")as file:
            for line in file:
                parts = line.strip().split(':')

                if len(parts) !=3:
                    updated_lines.append(line)
                    continue
                
                saved_user, saved_pass, role = parts
                if UserNAME == saved_user and Old_Password == saved_pass:
                    New_Password = input("Enter Your New Password: ")
                    updated_lines.append(f"{UserNAME}: {New_Password}:{role}\n")
                    found = True
                else:
                    updated_lines.append(line)
        if found:
            with open("login.txt", "w") as file:
                 file.writelines (updated_lines)
                 print("Password Changed Successfully")
        else:
            print("Incorrect User Name or Password.")

   except FileNotFoundError:
      print("Something Error Plese Try Again")

def main():
    role, username = login()
    if role is None:
        print("Login failed. Exiting. ")
    if role == "admin":
        Adminmenu()
    else:
        Usermenu()

main()


   

                    








 









    












  
