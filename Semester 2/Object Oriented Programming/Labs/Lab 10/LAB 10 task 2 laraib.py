class BankAccount:
    def __init__(self, minbal, curbal):
        self._minbal = minbal
        self._curbal = curbal

    def withdraw(self, amount):
        try:
            if amount > self._curbal - self._minbal:
                raise LowBalanceException
            else:
                self._curbal -= amount
                print(f'Your Withdrawal of amount {amount} is successful. Now your current balance is: {self._curbal}')
        except LowBalanceException:
            print(f'Your amount exceeds minimum balance requirement of the bank. Error: Low Balance Exception')

    def __str__(self):
        return f'\nCurrent balance: {self._curbal}\nMinimum balance: {self._minbal}.'


class LowBalanceException(Exception):
    def __str__(self):
        return 'Withtdrawal amount exceeds the available balance.'
    
def main():
    accounts = [
        BankAccount(50, 1000),
        BankAccount(500, 3000),
        BankAccount(450, 4000),
        BankAccount(800, 5000)
    ]
    for account in accounts:
        print(f'\nAccount details: {account}')
        account.withdraw(500)
        account.withdraw(100)
        account.withdraw(4500)
main()