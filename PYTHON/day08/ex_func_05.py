#-----
#사용자 정의 함수
#-----
#디폴트 매개변수 함수: 함수 호출 시 데이터가 전달되지 않을 때 미리 지정된 값으로 처리
# 형식: def 함수명(매개변수1, ..., 매개변수n,매개변수=0)

def add(num1=0,num2=0):
    return num1+num2
print(add())
print(add(5))
print(add(4,5))

#기능: 회원가입
#이름: register
#매개 변수: id,pw,gender(성별 기본값 '남' 지정)
#결과: OOO님 가입을 환영합니다! (str)
def register(gender='남',id,pw):
    return f'{id}님 가입을 환영합니다!'

#디폴트 매개변수는 젤 뒤에 와야 함
def register(id,pw,gender='남'):
    return f'{id}-{gender} 님 가입을 환영합니다!'

print(register('kk','k123'))
print(register('kk','k123','여'))

def test(n1,n2,*nums):
    print(n1,n2,nums)

test(1,2,3,4)