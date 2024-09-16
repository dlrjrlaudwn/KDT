#-----
#조건부 표현식: 조건문을 한줄로 축약(다중조건문 축약 시 사용/다른 프로그래밍 언어의 '삼항연산자'와 유사)0
# 형식: (참일 때 실행 코드) if 조건식 else (거짓시 실행 코드)
#-----
#임의의 숫자 데이터 정한 후 해당 숫자 데이터가 짝수인지 홀수인지 판별(%2 해서 0이면 짝수, 1이면 홀수)
num=209
#비교연산자
if num%2==0:
    print('짝수')
else: 
    print('홀수')

#값으로 조건 판별
if num%2:  #num%2했을 때 1이 나와야 True => 홀수/0이 나오면 False => 짝수
    print('홀수')
else: 
    print('짝수')

#not 연산자
if not num%2:  
    print('짝수')
else: 
    print('홀수')

#한줄로 축약: 조건부 표현식
print('짝수') if num%2==0 else print('홀수')
print('홀수') if num%2 else print('짝수')
print('짝수') if not num%2 else print('홀수')

