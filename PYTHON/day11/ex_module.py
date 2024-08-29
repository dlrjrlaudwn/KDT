import math  #이 파일에 모듈 포함시키기

#모듈 내의 변수, 함수, 클래스 사용: (모듈명).(변수/함수/클래스명)
# 1. 변수
math.pi
print(f'내장모듈 math 내 pi 변수: {math.pi}')
print(f'내장모듈 math 내 pi 변수: {pi}')
# 2. 함수
print(f'내장모듈 math 내 factorial 함수: {math.factorial(3)}')

#모듈명이 길면 줄여서 별칭으로 사용 가능
import random as rad
print(f'내장모듈 random 내 random 함수: {rad.random()}')
print(f'내장모듈 random 내 randint 함수: {random.randint()}')
