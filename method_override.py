# 일반 유닛
class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp 
    self.speed = speed
    
  def move(self, location):
    print('[지상 유닛 이동]')
    print('{} : {} 방향으로 이동합니다.'.format(self.name , location, self.speed))

# 일반 유닛
class AttackUnit(Unit):
  def __init__(self, name, hp, speed, damage): # 상속
    Unit.__init__(self, name, hp, speed) # 상속받은것을 정의해줘야함
    self.damage = damage
    
  def attack(self, location):
    print('{} : {} 방향으로 공격합니다. [공격력 {}]'.format(self.name, location, self.damage))
    
  def damaged(self, damage):
    print('{} : {} 데미지를 입었습니다.'.format(self.name, damage))
    self.hp -= damage
    print('{} : HP {}'.format(self.name, self.hp))
    if self.hp <= 0:
      print('{} has been destroied'.format(self.name))
      
# 날 수 있는 기능을 가진 클래스
class Flyable:
  def __init__(self, flying_speed):
    self.flying_speed = flying_speed
    
  def fly(self, name, location):
    print('{} : {} 방향으로 날아갑니다. [속도 {}]'.format(name, location, self.flying_speed))
    
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 다중상속
  def __init__(self, name, hp, damage, flying_speed):
    AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
    Flyable.__init__(self, flying_speed)
    
  def move(self, location):
    print('[공중 유닛 이동]')
    self.fly(self.name, location)
    
# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit('Vulture', 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력과 공격력 좋음
battlecruiser = FlyableAttackUnit('Battlecruiser', 500, 25, 3)

vulture.move('11시')
#battlecruiser.fly(battlecruiser.name, '9시')
battlecruiser.move('9시')