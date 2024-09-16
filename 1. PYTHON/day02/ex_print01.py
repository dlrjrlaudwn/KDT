#---------------------
#내장함수 print() 사용
# 모니터, 콘솔, 터미널에 출력하는 함수
# print(argument,..., n개)/print()
#---------------------

#나이, 이름, 성별 저장
age=100
name='마징가'
gender='남자'

#모니터에 출력
print(age)
print(name)
print(gender)

#한줄에 3개 모두 출력
print(age, name, gender)
print(99, '홍길동', '여자')

#2개의 정수 덧셈 결과 출력
num1=2
num2=9
print(num1+num2)

#출력 결과를 2+9=11 로 나오게끔
print(num1,'+', num2, '=', num1+num2)

#서식 지정자(format string) 방식
# 화면 출력 글자를 만들고 그 글자 안에 특정 결과 출력
# 글자 내부에 정수 결과 넣기: '%d' %변수명or수식
# 실수 f
# 글자 s
#2+9=11 출력
print('%d+%d=%d' %(num1, num2, num1+num2))

#9/2=4.5 출력
print('%d/%d=%f' %(num2, num1, num2/num1))
print('%s/%s=%s' %(num2, num1, num2/num1))

#f-string 방식
# 형식: f'  {변수명/수식/데이터}    '
#2+9=11 출력
print(f'{num1}+{num2}={num1+num2}')

#9/2=4.5 출력
print(f'{num2}/{num1}={num2/num1}')
