from Exercise_ch18_ch19_ch20 import *


if __name__ == "__main__":
    acc1 = CurrentAccount('123', 'John', 10.05, 100.0)
    acc2 = DepositAccount('345', 'John', 23.55, 0.5)
    acc3 = InvestmentAccount('567', 'Phoebe', 12.45,
                                    'high risk')
    print(acc1)
    print(acc2)
    print(acc3)
    acc1.deposit(23.45)
    acc1.withdraw(12.33)
    print('balance:', acc1.balance)
    print('Number of Account instances created:',
          Account.num_instance)
    print('balance:', acc1.balance)
    acc1.withdraw(300.00)
    print('balance:', acc1.balance)