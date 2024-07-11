import os

class BankAccount:

    balance = 0

    def deposit_money (self,):
        amount_deposit= int(input('ENTER DE AMOUNT OF MONEY YOU WANT TO DEPOSIT: '))
        self.balance =+ amount_deposit
        print('TRANSACTION COMPLETE')
        
    def withdraw_money (self,):
        amount_withdraw = int(input('ENTER DE AMOUNT OF MONEY YOU WANT TO WITHDRAW: '))
        min_ok = SavingAccount.minimum_Balance(self,amount_withdraw)
        if min_ok == 1:
            self.balance = self.balance - amount_withdraw
        else: 
            print('TRANSACTION NOT COMPLETE')


class SavingAccount(BankAccount):

    def minimum_Balance(self, amount_withdraw ,min_balance = 30):
        balance_before_withdraw= self.balance - amount_withdraw 
        if balance_before_withdraw <= min_balance:
            print('Balance too low, try later')
            return 2
        else: 
            return 1
    

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


ACCOUNT = BankAccount()
while True:

    action= int(input('BANK ACCOUNT\n PRESS 1 TO DEPOSIT \n PRESS 2 TO WITHDRAW\n PRESS 3 TO EXIT\n SELECT AN OPTION:')) 
    if action == 1:
        print (f'MONEY ON BACK ACCOUNT \n     ---{ACCOUNT.balance}---')
        ACCOUNT.deposit_money()
    elif action == 2:
        print (f'MONEY ON BACK ACCOUNT \n     ---{ACCOUNT.balance}---')
        ACCOUNT.withdraw_money()
    else: 
        break

    print (f'MONEY ON BACK ACCOUNT \n     ---{ACCOUNT.balance}---')
    input('PRESS ENTER TO CONTINUE')
    clear_screen()