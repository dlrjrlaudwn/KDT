#-----
#모듈: 변수, 함수, 클래스가 들어있는 파이썬 파일
# import 묘듈파일명(확장자 제외)
#패키지: 동일한 목적의 모듈들의 모음(패키지 안에는 여러 개의 모듈 파일 존재)
#-----
import random as rad #as ~ : ~로 줄여서 쓴다
rad.random()

#임의의 숫자 10개 생성
for cnt in range(10):
    print(int(rad.random()*10)) #[0,1): 0이상 1미만

for cnt in range(10): print(rad.randint(0,1))

#로또 프로그램: 1~45 중에서 중복없이 6개 추출
lotto=[0,0,0,0,0,0]
idx=0
while True:
    num=rad.randint(1,45)
    if num not in lotto:
        lotto[idx]=num
        idx=idx+1
    if idx==6: break

print(lotto)

lotto={}
key=1
while True:
    num=rad.randint(1,45)
    if num not in lotto.values():
        lotto[key]=num
        key=key+1
    if key==7: break

print(lotto.values())

lotto={}
key=1
while len(lotto)<6:
    num=rad.randint(1,45)
    if num not in lotto.values():
        lotto[key]=num
        key=key+1

print(lotto.values())

lotto=set()

while len(lotto)<6:
    num=rad.randint(1,45)
    num_set=set([num])
    lotto=lotto.union(num_set)

print(lotto)

#set타입의 add() 메서드: set에 원소 추가
lotto=set()
while len(lotto)<6:
    num=rad.randint(1,45)
    lotto.add(num)
print(lotto)