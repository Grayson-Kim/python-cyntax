for waiting_no in range(1, 6):
  print('number: {}'.format(waiting_no))
  
starbucks = ['aa','bb','cc']
for customer in starbucks:
  print('{}, your older is ready.'.format(customer))
  
  
students = ['Iron man', 'Thor', 'Grayson']
students = [len(i) for i in students]
print(students)