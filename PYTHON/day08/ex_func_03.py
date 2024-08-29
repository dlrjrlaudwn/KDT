#-----
#사용자 정의 함수
#-----
#매개변수의 개수를 유동적으로 할 수 있도록
# def 함수명(*변수명):

#기능: 정수를 덧셈한 후 결과 반환(리턴)하는 함수
#이름: add
#매개변수: n개
#결과: 덧셈 결과 값 result
def add(*nums):
    total=0
    for n in nums:
        total +=n
    return total

print(add())
print(add(1,1,1))
print(add(5,6))
print(add(8,9,11,22,55,11,6,7))