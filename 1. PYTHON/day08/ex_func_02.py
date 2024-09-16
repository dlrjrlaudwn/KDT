#-----
#사용자 정의 함수
#-----
#함수의 기능(역할) -> 이름 -> 매개 변수 -> 결과
# ex1) 기능: 2개의 정수를 덧셈한 후 결과 출력하는 함수
#      이름: add
#      매개 변수: 2개(num1, num2)
#      결과: 없음

def add(num1,num2):
    result=num1+num2
    print(f'{num1}+{num2}={result}')

add(5,8)

# ex2) 기능: 인사 메세지 출력 함수
#      이름: hello
#      매개 변수: 없음
#      결과: 없음

def hello():
    print('hello')

hello()

# ex3) 기능: 원하는 단의 구구단을 출력해주는 기능의 함수
#      이름: gg
#      매개 변수: 1개(dan)
#      결과: 없음

def gg(dan):
    for n in range(1,10): 
        print(f'{dan}*{n}={dan*n}')

gg(2)

# ex4) 기능: 파일의 확장자를 반환해주는 기능의 함수
#      이름: files
#      매개 변수: 1개(fname)
#      결과: 확장자(result)

def files(fname):
    data=fname.find('.')
    result=fname[data+1:]
    return result

f=files('hello.txt')
print(f)

def files(fname):
    return fname[fname.rfind('.')+1:]
