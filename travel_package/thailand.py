class ThailandPackage:
  def detail(self):
    print('태국 여행 : 50만원')
    
# 이 모듈이 내부에서 실행하는지 외부에서 호출하여 실행되는지 확인 가능
if __name__ == "__main__": # 이 라인을 외워야할듯
  print('Thailand 모듈을 직접 실행')
  trip_to = ThailandPackage()
  trip_to.detail()
else:
  print('Thailand 외부에서 모듈 호출')