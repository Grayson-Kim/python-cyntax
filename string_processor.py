#!/home/cabox/.pyenv/shims/python3
python = 'ABCD abcd abcd'
print(python.lower())
print(python.upper())
print(python[0].islower()) #False
print(python.replace('AB', 'ab'))

index = python.index('c')
print(index)
index = python.index('c', index + 1) # error if not exist
print(index)

print(python.find('d')) # return -1 if not exist

print(python.count('d'))