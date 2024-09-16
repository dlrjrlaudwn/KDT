#기능: 정수를 덧셈한 후 결과 반환
#이름: addInt
#매개변수: 가변인자(*)
#결과: 정수 result

def addInt(*nums):
    total=0
    for n in nums:
        total+=n
    return total

total=100

def multiInt(*nums):
    total1=1
    for n in nums: total1*=n
    return total1+total

result1=addInt(1)
print(f'result1:{result1}')

result2=multiInt(5)
print(f'result2:{result2}')

#전역변수의 값을 변경: global ()
def multiInt2(*nums):
    global total
    for n in nums: total*=n
    return total

print(f'전:total => {total}')
result2=multiInt2(5)
print(f'result2:{result2}')

print(f'후:total => {total}')