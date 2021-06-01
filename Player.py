from Hand import Hand
from account import Account


class User:
    def __init__(self, user_name, account_balance: 0):
        self.account = Account(account_balance, user_name)
        self.hand = Hand()

    def hit_or_stand(self):
        pass

    def show_cards(self, num):
        pass


class Human(User):
    def __init__(self, user_name, account_balance=100):
        User.__init__(user_name, account_balance)

    def hit_or_stand(self):
        print(f'Your current hand is {self.hand.value}')
        return input('Do you want to hit(1) or stand(2)?')

    def show_cards(self, num=None):
        print(self.hand.get_cards_str())

    def place_bet(self, amount):
        pass


class Dealer(User):
    def __init__(self):
        User.__init__(user_name='Mr. Fat')

    def hit_or_stand(self):

        if self.hand.value < 17:
            return 1
        else:
            return 2

    def show_cards(self, num):
        print(self.hand.get_cards_str(num))

