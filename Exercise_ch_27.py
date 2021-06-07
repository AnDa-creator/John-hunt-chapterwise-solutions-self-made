import fintech.accounts as accounts

if __name__ == "__main__":
    with accounts.CurrentAccount('891', 'Adam', 5.0, 50.0) as acc:
        acc.deposit(23.0)
        acc.withdraw(12.33)
        print(acc.balance)