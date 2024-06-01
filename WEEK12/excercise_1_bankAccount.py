import os

def clear_screen ():
    os.system('cls' if os.name == 'nt' else 'clear')

class SavingAccount:

    def __init__ (self,balance,amount):

        self.min_balance = 100

        if balance >= (self.min_balance +  amount):
            return True
        else:
            return False 

class BankAccount (SavingAccount): 
    
    def __init__ (self):
        self.balance = 0

    def enter_money (self,amount):
        self.balance += amount
        clear_screen()
        input(f"SUCCESSFULLY TRANSACTION BALANCE ON ACCOUNT {self.balance}\n PRESS ENTER TO CONTINUE \n")
    
    def withdrawal_money (self,amount):
        transaction_approved = SavingAccount.__init__(self,self.balance,amount)
        if transaction_approved == True:
            self.balance -= amount
            clear_screen()
            input(f"SUCCESSFULLY TRANSACTION BALANCE ON ACCOUNT {self.balance} \n PRESS ENTER TO CONTINUE \n")
        else:
            input("THE BALANCE IS TOO LOW, PRESS ENTER TO CONTINUE")

account = BankAccount()

while True:
    try:
        clear_screen()
        operation = int(input("PLEASE ENTRE 1 TO ENTER MONEY OR 2 TO MAKE A WITHDRAWAL\n ENTER AN OPTION: "))
        if operation == 1:
            amount_of_money = int(input("PRESS THE AMOUNT TO ENTRY : "))
            account.enter_money(amount_of_money)
        elif operation == 2:
            amount_of_money = int(input("PRESS THE AMOUNT TO WITHDRAWAL: "))  
            account.withdrawal_money(amount_of_money)
    except ValueError as error:
        input("INVALID INPUT, PLEASE ENTER A CORRECT VALUE, PRESS ENTER TO CONTINUE.\n ")



