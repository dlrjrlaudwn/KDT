#모듈 내에서 일부 변수, 함수, 클래스만 포함하는 경우: from 모듈명 import 변수/함수/클래스

#math모듈에서 pi변수만 가져오기
from math import pi

# 사용: 바로 변수/함수/클래스명으로 사용
print(f'내장모듈 math 안에 있는 pi 변수 사용: {pi}')
#print(math.factorial())

from math import pi, factorial
print(f'내장모듈 math 안에 있는 pi 변수 사용: {pi}')
#print(factorial())

#전역변수
pi='apple'
print(f'내장모듈 math 안에 있는 pi 변수 사용: {pi}')

#random 모듈 내에 있는 거 다 가져와
from random import *

#import와 차이점: '(모듈명).' 안 써도 됨