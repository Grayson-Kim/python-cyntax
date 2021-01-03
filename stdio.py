print('python', 'java', sep=',', end='?') # end=' '  끝 문자를 이것으로 바꿔라.(자동줄바꿈안됨)
print('what would be more interesting?')

scores = {'math':0, 'English':50, 'coding':100}
for subject, score in scores.items():
  print(subject.ljust(8), str(score).rjust(4), sep=':')
  
for num in range(1,10):
  print('Num: ' + str(num).zfill(3)) # 값이 없는것은 0으로 채움. (3)만큼