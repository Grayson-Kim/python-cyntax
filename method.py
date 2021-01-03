class Unit:
  def __init__(self, name, hp):
    self.name = name
    self.hp = hp 
    
class AttackUnit(Unit):
  def __init__(self, name, hp, damage): # 상속
    Unit.__init__(self, name, hp) # 상속받은것을 정의해줘야함
    self.damage = damage
    
  def attack(self, location):
    print('{} : {} 방향으로 공격합니다. [공격력 {}]'.format(self.name, location, self.damage))
    
  def damaged(self, damage):
    print('{} : {} 데미지를 입었습니다.'.format(self.name, damage))
    self.hp -= damage
    print('{} : HP {}'.format(self.name, self.hp))
    if self.hp <= 0:
      print('{} has been destroied'.format(self.name))
      
firebat1 = AttackUnit('Firebat', 50, 16)
firebat1.attack('5시')

firebat1.damaged(25)
firebat1.damaged(25)

# 날 수 있는 기능을 가진 클래스
class Flyable:
  def __init__(self, flying_speed):
    self.flying_speed = flying_speed
    
  def fly(self, name, location):
    print('{} : {} 방향으로 날아갑니다. [속도 {}]'.format(name, location, self.flying_speed))
    
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 다중상속
  def __init__(self, name, hp, damage, flying_speed):
    AttackUnit.__init__(self, name, hp, damage)
    Flyable.__init__(self, flying_speed)
    
# 공중 공격 유닛
valkyrie = FlyableAttackUnit('발키리', 200, 6, 5)
valkyrie.fly(valkyrie.name, '3시')