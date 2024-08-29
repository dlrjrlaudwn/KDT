#-----
#반복문과 continue문
# : continue 구문을 만나면 아래 코드 실행 X & 반복문으로 돌아가서 다음 요소 데이터를 가지고 진행
#-----
#1~50 숫자로 구성된 데이터 중 3의 배수만 출력
data=range(1,51)
for d in data:
    if d%3==0:
        print(d)

for d in data:
    if d%3: continue
    print(d)