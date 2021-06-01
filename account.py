import random
import sys


class Account:
    def __init__(self, balance, owner):
        # private
        self.__balance = balance
        self.__minimum_deposit = 5

        # public
        self.owner = owner

    # take money out
    def withdraw(self, amount_to_withdraw, quiet=True):

        if amount_to_withdraw > self.__balance:
            if not quiet:
                print('You cannot withdraw more than you have!')
        else:
            self.__balance -= amount_to_withdraw

    # put money in
    def deposit(self, amount_to_deposit):
        self.__balance += amount_to_deposit

    # getter
    def get_balance(self):
        return self.__balance


if __name__ == '__main__':
    account = Account(0, 'Jerry')
    account.deposit(10)
    account.withdraw(100)
    print(account.get_balance())
