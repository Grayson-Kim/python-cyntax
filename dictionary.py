cabinet = {3:'you', 100:'me', 'aa':'jinook'} #dictionary 자료형 사용법
print(cabinet[3])
print(cabinet[100]) #값이 없으면 오류
print(cabinet.get(3)) #값이 없으면 None 출력
print(cabinet.get('aa'))

print(3 in cabinet) # True
print(5 in cabinet) # False

# add or update keys
cabinet['aa'] = 'gray'

# print keys only
print(cabinet.keys())

# print values only
print(cabinet.values())

# print both keys and values
print(cabinet.items())

# delete all
cabinet.claer()