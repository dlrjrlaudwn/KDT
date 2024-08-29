#-----
#함수 이해 및 활용
#-----
#기능: 3개의 정수를 덧셈&결과 반환
#이름: add3
#매개변수: num1,num2,num3
#결과: result

def add3(num1,num2,num3):
    result=num1+num2+num3
    return result

#기능: 3개의 정수를 곱셈&결과 반환
#이름: multi3
#매개변수: num1,num2,num3
#결과: result

def multi3(num1,num2,num3):
    result=num1*num2*num3
    return result

#기능: 2개의 정수를 나눗셈&결과 출력
#이름: div
#매개변수: num1,num2
#결과: None

def div(num1,num2):
    if not num2:
        result='0으로 나눌 수 없음'
    else:
        result=num1/num2
    print(f'{num1}/{num2}={result}')

#함수 사용하기: 호출
value=add3(1,2,3) 

value1=div(3,4)
print(value1)