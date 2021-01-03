'''
import travel_package.thailand # 클레스나 함수는 바로 import 불가
trip_to = travel_package.thailand.ThailandPackage()
trip_to.detail()

from travel_package.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel_package import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from travel_package import *
trip_to = vietnam.VietnamPackage()
trip_to1 = thailand.ThailandPackage()
trip_to.detail()
trip_to1.detail()
'''

from travel_package import *
import inspect, random, os
print(inspect.getfile(random))
print(inspect.getfile(thailand))