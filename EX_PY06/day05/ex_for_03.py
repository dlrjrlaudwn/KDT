#-----
#출력하고 싶은 단을 입력 받아서 해당 단의 구구단 출력
# ex) 입력:2단 -> 출력: 2*1=2
#-----
num=int(input())
nums=range(1,10)
for n in nums:
    print(f'{num}*{n}={num*n}')

for n in range(1,10):
    print(f'{num}*{n}={num*n}')
