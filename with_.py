'''import pickle

with open('profile.pickle','rb') as profile_file: # 파일을 닫지 않아도 자동종료
  print(pickle.load(profile_file))'''

'''with open('study.txt', 'w', encoding='utf8') as study_file:
  study_file.write('Im studying python')'''

with open('study.txt', 'r', encoding='utf8') as study_file:
  print(study_file.read())