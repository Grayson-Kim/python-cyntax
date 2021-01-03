from random import *
print(random()) # print 0~1 미만

print(randrange(1,46)) # 1~45
print(randint(1,45)) # 1~45

lst = [1,2,3,4,5]
shuffle(lst) # 리스트를 섞는다
print(lst)

print(sample(lst, 1)) # 랜덤으로 하나를 뽑는다.