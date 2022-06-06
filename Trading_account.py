import random

class Account:
    account_balance_list =[0]

    def create_account(self):
        global balance
        global account_details
        balance =0
        account_number = str(random.randint(10**11,10**12 -1)) 
        print(f'Account is created with account number {account_number}')
        account_details = {account_number:balance}
        return account_details

    def transfer_money(self,amount):
        account_number = input("please enter the account number: ")
        account_details[account_number] +=amount
        new_balance = account_details[account_number]
        self.account_balance_list.append(new_balance)
    
        return f'${amount} credited to your account {account_number}. New account balance: ${new_balance}'

    def withdraw_money(self,amount):
        account_number = input("please enter the account number: ")
        if amount < account_details[account_number]:

            account_details[account_number] -=amount
            new_balance = account_details[account_number]
            self.account_balance_list.append(new_balance)
        else:
            return "Your account doesn't have enough fund!"

        return f'${amount} debited from your account {account_number}. New account balance: ${new_balance}'
        