customer = 'gray'
index = 5
while index >= 1:
  print('{}, your older is ready. {} times left.'.format(customer, index))
  index -= 1
  if index == 0:
    print("your older has been destroied")