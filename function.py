def deposit(balance, money):
  print('you have {}$'.format(balance))
  return balance + money

balance = 100
balance = deposit(balance, 1000)
print(balance)