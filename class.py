class Unit:
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage
    print('{} 유닛이 생생 되었습니다.'.format(self.name))
    print('체력 {}, 공격력 {}'.format(self.hp, self.damage))
    
'''marine1 = Unit('마린', 40, 5)
marine2 = Unit('마린', 40, 5)
tank = Unit('탱크', 150, 35)'''

wraith1 = Unit('Wraith', 80, 5)
print('unit name : {}, AD : {}'.format(wraith1.name, wraith1.damage))
wraith1.clocking = True # 객체에 새로운 변수 추가 가능함

if wraith1.clocking == True:
  print('{} is corrently clocking.'. format(wraith1.name))