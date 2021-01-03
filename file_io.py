'''score_file = open('score.txt', 'w', encoding='utf8')
print('Math : 0', file=score_file)
print('English : 50', file=score_file)
score_file.close()'''

'''score_file = open('score.txt', 'a', encoding='utf8') # 이어쓰기
score_file.write('science : 80\n')
score_file.write('coding : 100')
score_file.close()'''

'''score_file = open('score.txt', 'r', encoding='utf8') # 모두 읽어오기
print(score_file.read())
score_file.close()'''

'''score_file = open('score.txt', 'r', encoding='utf8')
print(score_file.readline(), end='') # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end='')
print(score_file.readline(), end='')
print(score_file.readline(), end='')
score_file.close()'''

'''score_file = open('score.txt', 'r', encoding='utf8')
while True:
  line = score_file.readline()
  if not line:
    break
  print(line, end='')
print()
score_file.close()'''

score_file = open('score.txt', 'r', encoding='utf8')
lines = score_file.readlines() # list 형태로 저장
for line in lines:
  print(line, end='')
print()
score_file.close()