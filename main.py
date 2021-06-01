from account import Account
from Hand import Hand
from cards import Card
account = Account(0, 'Jerry')
account.withdraw(10)
print(account.get_balance())