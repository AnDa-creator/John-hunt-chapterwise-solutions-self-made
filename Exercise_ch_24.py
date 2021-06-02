from Exercise_ch18_ch19_ch20 import *


class AmountError(Exception):
    def __init__(self, account, error):
        self.account = account
        self.error = error

    def __str__(self):
        return 'AmountError ({}) on {}'.format(self.error, self.account)


class BalanceError(Exception):
    def __init__(self, account):
        self.account = account

    def __str__(self):
        return 'BalanceError (exceeds withdrawal limit) on {}'.format(self.account)


if __name__ == "__main__":
    acc1 = CurrentAccount('123', 'John', 10.05, 100.0)
    try:
        acc1.deposit(-1)
    except AmountError as e:
        print(e)
    finally:
        try:
            print('balance:', acc1.balance)
            acc1.withdraw(300.00)
            print('balance:', acc1.balance)
        except BalanceError as e:
            print('Handling Exception')
            print(e)
