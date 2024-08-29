#3.7 연습문제: 문자열 출력하기
print('Python Programming')

#3.8 심사문제: 문자열 출력하기
print('Hello, world!')
print('Hello, world!')

#5.5 연습문제: 아파트에서 소음이 가장 심한 층수 출력하기
print(int(0.2467*12+4.159))

#5.6 심사문제: 스킬 공격력 출력하기
print(102*0.6+225)

#6.6 연습문제: 정수 세 개를 입력받고 합계 출력하기
a=-10
b=20
c=30

print(a+b+c)

#6.7 심사문제: 변수 만들기
a=50
b=100
c='None'

print(a)
print(b)
print(c)

#6.8 심사문제: 평균 점수 구하기
a=int(input('국어'))
b=int(input('영어'))
c=int(input('수학'))
d=int(input('과학'))

print(int((a+b+c+d)/4))

#7.4 연습문제: 날짜와 시간 출력하기
year=2000
month=10
day=27
hour=11
minute=43
second=56

print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')

#7.5 심사문제: 날짜와 시간 출력하기
year, month, day, hour, minute, second=input().split()
print(year, month, day, sep='-', end='T')
print(hour, minute, second, sep=':')

#8.4 연습문제: 합격 여부 출력하기
korean=92
english=47
mathmatics=86
science=81

print(korean>=50 and english>=50 and mathmatics>=50 and science>=50)

#8.5 심사문제: 합격 여부 출력하기
korean, english, mathmatics, science=map(int, input().split())
print(korean>=90 and english>80 and mathmatics>85 and science>=80)