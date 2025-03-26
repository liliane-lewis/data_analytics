#!/usr/bin/python3

#Exercise 1: Bank Account
#Instructions
#
#Part I:
#
#    Create a class called BankAccount that contains the following attributes and methods:
#        balance - (an attribute)
#        __init__ : initialize the attribute
#        deposit : - (a method) accepts a positive int and adds to the balance, raise an Exception if the int is not positive.
#        withdraw : - (a method) accepts a positive int and deducts from the balance, raise an Exception if not positive
##

#Part II : Minimum balance account
#
#    Create a MinimumBalanceAccount that inherits from BankAccount.
#    Extend the __init__ method and accept a parameter called minimum_balance with a default value of 0.
#    Override the withdraw method so it only allows the user to withdraw money if the balance remains higher than the minimum_balance, 
#    raise an Exception if not.
#
#
#Part III: Expand the bank account class
#
#    Add the following attributes to the BankAccount class:
#        username
#        password
#        authenticated (False by default)
#
#    Create a method called authenticate. This method should accept 2 strings : a username and a password. 
# If the username and password match the attributes username and password the method should set the
#  authenticated boolean to True.#
#
#    Edit withdraw and deposit to only work if authenticated is set to True, if someone tries an action without being 
# authenticated raise an Exception
#
#
#Part IV: BONUS Create an ATM class
#
#   __init__:
#        Accepts the following parameters: account_list and try_limit.#
#
#        Validates that account_list contains a list of BankAccount or MinimumBalanceAccount instances.
#        Hint: isinstance()
#
#        Validates that try_limit is a positive number, if you get an invalid input raise an Exception, 
#        then move along and set try_limit to 2.
#        
# Hint: Check out this tutorial#
#
#        Sets attribute current_tries = 0
#
#        Call the method show_main_menu (see below)
#
#    Methods:
#        show_main_menu:
#            This method will start a while loop to display a menu letting a user select:
#                Log in : Will ask for the users username and password and call the log_in method with the username and password (see below).
#                Exit.
#
#        log_in:
#            Accepts a username and a password.
#
#            Checks the username and the password against all accounts in account_list.
#                If there is a match (ie. use the authenticate method), call the method show_account_menu.
#                If there is no match with any existing accounts, increment the current tries by 1. Continue asking the user for a username 
# and a password, until the limit is reached
# (ie. try_limit attribute). Once reached display a message saying they reached max tries and shutdown the program.
#
#        show_account_menu:
#            Accepts an instance of BankAccount or MinimumBalanceAccount.
#            The method will start a loop giving the user the option to deposit, withdraw or exit.


class BankAccount:

    def __init__(self, username, password, balance=0, authenticated=False):

        if not isinstance(balance, int):
            raise ValueError("Initial balance must be an integer")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            print(f"{self.username} authenticated successfully.")
            return True
        return False

    def deposit(self, value):
        if not self.authenticated:
            raise ValueError("The user must be authenticated")
        if value <= 0:
            raise ValueError("Deposit must be a positive amount")
        self.balance += value

        
    def withdraw(self, value):
        if not self.authenticated:
            raise ValueError("iThe user must be authenticaded")
        if value <= 0:
            raise ValueError("Withdraw must be a positive amount")
        if value > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= value

    def get_balance(self):
        return self.balance
    
class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance=balance)
        if minimum_balance < 0:
            raise ValueError("Minimum balance cannot be negative")
        self.minimum_balance = minimum_balance

    def withdraw(self, value):
        if not self.authenticated:
            raise ValueError("User must be authenticated")
        if value <= 0:
            raise ValueError("Withdraw must be a positive amount")
        if self.balance - value < self.minimum_balance:
            raise ValueError("Withdrawal denied: balance would fall below the minimum required")
        self.balance -= value

class ATM:
    def __init__(self, account_list, try_limit=2):
        if not isinstance(account_list, list) or not all(isinstance(acc, BankAccount) for acc in account_list):
            raise ValueError("account_list must be a list of BankAccount or MinimumBalanceAccount")
        if not isinstance(try_limit, int) or try_limit <= 0:
            print("Invalid try_limit provided, defaulting to 2.")
            try_limit = 2

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.current_user = None
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n1 - Log In")
            print("2 - Exit")
            choice = input("Choose an option: ")

            if choice == "2":
                print("Goodbye.")
                break
            elif choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                self.log_in(username, password)
            else:
                print("Invalid option.")

    def log_in(self, username, password):
        for account in self.account_list:
            if account.authenticate(username, password):
                self.current_user = account
                self.show_account_menu(account)
            #return  

        self.current_tries += 1
        print("Invalid credentials.")
        if self.current_tries >= self.try_limit:
            print("Too many failed attempts. Shutting down.")
            exit()

    def show_account_menu(self, account):
        while True:

            print("\n1 - Deposit")
            print("2 - Withdraw")
            print("3 - Check Balance")
            print("4 - Logout")
            choice = input("Choose an option: ")

            try:
                if choice == "1":
                    amount = int(input("Enter amount to deposit: "))
                    account.deposit(amount)
                    print("Deposit successful.")
                    #print(f"Balance: {account.balance}")
                elif choice == "2":
                    amount = int(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                    print("Withdrawal successful.")
                    print(f"Balance: {account.balance}")
                elif choice == "3":
                    print(f"Current balance: {account.get_balance()}")
                elif choice == "4":
                    print("Logging out.")
                    return
                else:
                    print("Invalid option.")
            except ValueError as e:
                print("Error:", e)

        


acc1 = BankAccount("user1", "pass1", balance = 100)
acc2 = MinimumBalanceAccount("user2", "pass2", 200 , 50)
acc3 = MinimumBalanceAccount("user3", "pass3", 10000 , 500)

atm = ATM([acc1, acc2, acc3],30)
