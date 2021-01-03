import pickle
'''profile_file = open('profile.pickle', 'wb')
profile = {'name':'Gray', 'age':20, 'hobby':['soccor','game','coding']}
print(profile)
pickle.dump(profile, profile_file) # profile 에 있는 정보를 profile_file 파일에 저장
profile_file.close()'''

profile_file = open('profile.pickle', 'rb')
profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()