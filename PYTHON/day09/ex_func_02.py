#ㄱㅖ산기 만들기
#사칙연산 기능별 함수 생성(+ - * /), 2개의 정수만 계산

def plus(num1,num2):
    return num1+num2

def minus(num1,num2):
    return num1-num2

def mult(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2 if num2 else '0으로 나눌 수 없음'

i=input().split()

if i=='+': plus(i[0],i[-1])
elif i=='-': minus(i[0],i[-1])
elif i=='*': mult(i[0],i[-1])
elif i=='/': div(i[0],i[-1])

print(i)

#사용자가 종료를 원할 때 종료 => 'x' and 'X' 입력시 종료
#연산방식과 숫자 데이터 입력 받기: while

while True:
    #입력
    req=input('연산방식과 정수 2개 입력(ex.+ 10 2):') 
    #종료
    if req=='x' or 'X':
        print('계산기를 종료합니다.')
        break
    #연산방식&데이터 추출
    op,n1,n2=req.split()
    #str -> int 변환
    n1=int(n1)
    n2=int(n2)
    #계산
    if op=='+':print(f'{n1}+{n2}={plus(n1,n2)}') 
    elif op=='-':print(f'{n1}-{n2}={minus(n1,n2)}') 
    elif op=='*':print(f'{n1}*{n2}={mult(n1,n2)}') 
    elif op=='/':print(f'{n1}/{n2}={div(n1,n2)}') 
    else: print(f'{op}는 지원하지 않는 연산입니다.')
