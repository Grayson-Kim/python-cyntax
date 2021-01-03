try:
  print('나누기 전용 계산기입니다.')
  nums = []
  nums.append(int(input('첫 번째 숫자를 입력하세요 : ')))
  nums.append(int(input('두 번째 숫자를 입력하세요 : ')))
  #nums.append(int(nums[0] / nums[1])) # 만약 실수로 빠트렸을 경우 테스트
  print('{} / {} = {}'.format(nums[0], nums[1], nums[2]))
except ValueError:
  print('에러! 잘못된 값을 입력하셨습니다.')
except ZeroDivisionError as err:
  print(err)
except Exception as err:
  print(str(err)+' 애러가 발생하였습니다.')
except:
  print('알 수 없는 애러가 발생하였습니다.')