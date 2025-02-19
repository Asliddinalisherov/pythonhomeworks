import random

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
class Bank:
    def __init__(self):
        self.accounts = dict()
        self.used_account_numbers = set()
    
    def generate_unique_account_number(self):
        while True:
            account_number = random.randint(1000, 9999)
            if account_number not in self.used_account_numbers:
                self.used_account_numbers.add(account_number)
                return account_number
    
    def create_account(self, name, initial_deposit):
        account_number = self.generate_unique_account_number()
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        print(f'Account created successfully. Account number: {account_number}')
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f'Account number: {account.account_number}, Name: {account.name}, Balance: {account.balance}')
        else:
            print('Account not found.')
    
    def deposit(self, account_number, deposit):
        account = self.accounts.get(account_number)
        if account:
            account.balance += deposit
            print(f'Deposit successful. New balance: {account.balance}')
        else:
            print('Account not found.')
        
    def withdraw(self, account_number, withdawal):  
        account = self.accounts.get(account_number)
        if account:
            account.balance -= withdawal
            print(f'Withdrawal successful. New balance: {account.balance}')
        else:
            print('Account not found.')
    
    def save_to_file(self):
        with open('accounts.txt', 'w') as f:
            for account in self.accounts.values():
                f.write(f'{account.account_number},{account.name},{account.balance}\n')
        print('Accounts saved successfully.')
    
    def load_from_file(self):
        with open('accounts.txt') as f:
            for line in f:
                account_number, name, balance = line.strip().split(',')
                self.accounts[int(account_number)] = Account(int(account_number), name, float(balance))
        print('Accounts loaded successfully.')

bank = Bank()
while True:
    choice = input('Enter your choice: ')
    if choice == '1':
        name = input('Enter your name: ')
        initial_deposit = float(input('Enter initial deposit: '))
        bank.create_account(name, initial_deposit)
    elif choice == '2':
        account_number = int(input('Enter account number: '))
        bank.view_account(account_number)
    elif choice == '3':
        account_number = int(input('Enter account number: '))
        deposit = float(input('Enter deposit amount: '))
        bank.deposit(account_number, deposit)
    elif choice == '4':
        account_number = int(input('Enter account number: '))
        withdrawal = float(input('Enter withdrawal amount: '))
        bank.withdraw(account_number, withdrawal)
    elif choice == '5':
        bank.save_to_file()
    elif choice == '6':
        bank.load_from_file()
    else:
        break