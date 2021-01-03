gun = 10

def checkpoint(soldiers):
  global gun # 전역 공간에 있는 gun 사용
  gun = gun - soldiers
  
checkpoint(2)
print('number of guns: {}'.format(gun))