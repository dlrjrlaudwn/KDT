#덧셈,뺄셈,곱셈,나눗셈 함수 각각 만들기
#매개변수: 정수 2개(num1,num2)
#결과: 연산 결과 반환

def plus(num1,num2):
    return num1+num2

def minus(num1,num2):
    return num1-num2

def mult(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2 if num2 else '0으로 나눌 수 없음'

#함수 사용하기(호출)
print(div(10,0))

#기능: 입력 데이터가 유효한 데이터인지 확인
#이름: check_data
#매개변수: 문자열 데이터/개수/구분자(data,count,sep='')
#결과: True/False
def check_data(data,count,sep=' '):
    if len(data):
        data2=data.split(sep)
        return True if count==len(data2) else False
    else: return False

print(check_data('+ 10 3',3))
print(check_data('+ 10',3))
print(check_data('+,10,3',3,','))


#사용자로부터 연산자, 숫자 1, 숫자 2를 입력 받아서 연산 결과 출력하기
x1,num1,num2=input('연산자,숫자1,숫자2:').split(',')  #언패킹으로 데이터 받기
num1,num2=map(int,(num1,num2))
if x1=='+': print(plus(num1,num2))
elif x1=='-': print(minus(num1,num2))
elif x1=='*': print(mult(num1,num2))
else: print(div(num1,num2))

op,num1,num2=input('연산자,숫자1,숫자2:').split()
if op not in ['+','-','*','/']: print(f'{op} 잘못된 연산자입니다.')
else:
    if num1.isdecimal() and num2.isdecimal():
        num1=int(num1)
        num2=int(num2)
        result=0
        if op =='+': result=plus(num1,num2)
        elif op=='-':result=minus(num1,num2)
        elif op=='*':result=mult(num1,num2)
        else:result=div(num1,num2)
        print(f'{num1}{op}{num2}={result}')
    else: print('정수만 입력 가능합니다.')