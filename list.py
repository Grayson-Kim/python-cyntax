num = [10,20,30]
print(num)
print(num.index(20))

num.append('add')
print(num)

num.insert(1, 'second')
print(num)

print(num.pop())
print(num)

print(num.count('second'))

#정렬
num_list = [3,2,4,5,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

#delete all
#num_list.clear()

#리스트 확장
num_list.extend(num)
print(num_list)