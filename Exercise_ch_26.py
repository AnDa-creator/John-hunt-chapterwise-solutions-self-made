from abc import ABCMeta, abstractmethod
from Exercise_ch_24 import *


class Account(metaclass=ABCMeta):
    num_instance = 0

    def __init__(self, ac_number, name, op_balance, ac_type=None):
        self.name = name
        self.ac_number = ac_number
        if op_balance >= 0:
            self._balance = op_balance
        else:
            raise ValueError
        self.ac_type = ac_type
        Account.num_instance += 1

    @property
    def balance(self):
        """This is for balance property"""
        return self._balance

    @abstractmethod
    def __str__(self):
        pass

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print("Withdrawn an amount of: ", amount, "current balance: ", self._balance)
        else:
            raise AmountError(self.__str__(), "Withdraw not possible")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("Deposited an amount of: ", amount, "Current Balance: ", self._balance)
        else:
            raise AmountError(self.__str__(), "Deposit not possible")

    def get_balance(self):
        return self._balance


class CurrentAccount(Account):
    def __init__(self, ac_number, name, op_balance, overdraft_limit):
        super().__init__(ac_number, name, op_balance)
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        return "Account[{}]: - {} , Current account = {} , overdraft limit = = {}".format(
            self.ac_number, self.name, self._balance, -self.overdraft_limit)

    def withdraw(self, amount):
        if self._balance - amount <= -self.overdraft_limit:
            raise BalanceError(self.__str__())
        else:
            super().withdraw(amount)


class DepositAccount(Account):
    def __init__(self, ac_number, name, op_balance, interest_rate):
        super().__init__(ac_number, name, op_balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return "Account[{}]: - {} , Deposit account = {} , Interest rate = {}".format(
            self.ac_number, self.name, self._balance, self.interest_rate)


class InvestmentAccount(Account):
    def __init__(self, ac_number, name, op_balance, investment_type):
        super().__init__(ac_number, name, op_balance)
        self.investment_type = investment_type

    def __str__(self):
        return "Account[{}]: - {} ,  Investment account = {}, Investment type = {}".format(
            self.ac_number, self.name, self._balance, self.investment_type)


if __name__ == "__main__":
    # TODO: uncomment next line to see that object instantiation is not possible
    # acc1 = Account('123', 'John', 10.05, 'current')
    acc1 = CurrentAccount('123', 'John', 10.05, 100.0)
    acc2 = DepositAccount('345', 'John', 23.55, 0.5)
    acc3 = InvestmentAccount('567', 'Phoebe', 12.45, 'high risk')
    acc1.deposit(23.45)
    acc1.withdraw(12.33)
    print('balance:', acc1.get_balance())
    acc1.withdraw(300.00)
    print('balance:', acc1.get_balance())
