# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {'a', 'b', 'c'}
python = set(['a', 'd'])

# 교집합 출력
print(java & python)
print(java.intersection(python))

# 합집합 출력
print(java | python)
print(java.union(python))

#차집합
print(java - python)
print(java.difference(python))

java.add('gg')

python.remove('b')