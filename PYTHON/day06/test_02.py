#-----
#숫자 데이터 10개를 입력 받아서 다 더한 후 합이 30이상이면 종료
#-----
total=0
for cnt in range(10):
    data=int(input())
    total=total+data
    if total>=30: break

