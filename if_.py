weather = input('how\'s the weather? ')
if weather == 'rain' or weather == 'snow':
  print('bring your umbrella')
elif weather == 'sunny':
  print('no need to bring')
  
temp = int(input("temperture: "))
if 30 <= temp:
  print('it is hot outside')
elif 10 <= temp < 30:
  print('good day')