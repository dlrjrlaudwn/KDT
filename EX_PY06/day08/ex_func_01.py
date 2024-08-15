#-----
#사용자 정의 함수
#-----
#함수의 기능(역할) -> 이름 -> 매개 변수 -> 결과
# ex) 기능: 2개의 정수를 덧셈한 후 결과 반환(return)하는 함수
#     이름: add
#     매개 변수: 2개(num1, num2)
#     결과: 덧셈 계산 값(result)

def add(num1,num2):
    result=num1+num2
    return result

#함수 호출: 함수 사용하기
# 함수명(데이터1, ..., 데이터 n)
value=add(10,20)
print(value)

#함수의 매개 변수 개수와 다른 데이터 전달: error
value=add(10,20,30)
print(value)

value=add(10)
print(value)