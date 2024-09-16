#-----
#반복문&조건문 혼합
#-----
# 1~50까지의 데이터 중 3의 배수((숫자)%3==0)는 제곱을 하고 나머지는 그대로해서 다 더해서 합계 출력
datas=range(1,51)
total=0
for data in datas:
    #3의 배수 확인
    if data%3:
        total=total+data       #3의 배수 아니니까 그대로
    else:
        total=total+(data*data)  #3의 배수는 제곱
print(f'합계:{total}')

#메시지에서 알파벳과 숫자를 구분해서 처리하기
# 알파벳은 ★, 숫자는 ♡로 변경해서 출력
msg='good 2024'
msg2=''
for m in msg:
    if ('a'<=m<='z') or ('A'<=m<='Z'):
        msg2=msg2+'★'
        print('★',end='')
    elif '0'<=m<='9':
        msg2=msg2+'♡'
        print('♡',end='')
    else:
        msg2=msg2+m
        print(m, end='')
print(f' msg2:{msg2}') 

