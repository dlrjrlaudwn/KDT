#-----
#반복문과 break: 중첩 반복문일 경우 가낭 가까이 있는 반복문만 break로 종료됨
#-----
#단의 숫자만큼 구구단 출력 ex) 2단:2*1=2 2*2=4 / 3단:3*1=3 3*2=6 3*3=9
dan=int(input())
isbreak=False

for d in range(2,10):
    print(f'\n[{d}단]',end=' ')
    for n in range(1,10):
        print(f'{d}*{n}={d*n:<2}',end=' ')   # :(숫자) <= 결과를 (숫자)자리로 설정(오른쪽 정렬이 기본/왼쪽 정렬하려면 :<(숫자))
        if n==d:
            isbreak=True
            break
    print('done')
    if isbreak:break

dan=int(input())
for d in range(2,dan+1):
    print(f'\n[{d}단]',end=' ')
    for n in range(1,d+1):
        print(f'{d}*{n}={d*n:<2}',end=' ')

dan=int(input())
for d in range(2,10):
    print(f'\n[{d}단]',end=' ')
    for n in range(1,10):
        print(f'{d}*{n}={d*n:<2}',end=' ')   # :(숫자) <= 결과를 (숫자)자리로 설정(오른쪽 정렬이 기본/왼쪽 정렬하려면 :<(숫자))
        if n==d: break
    if d==dan: break


#중첩 반복문에서 내부 반복문 종료 시 외부 반복문도 종료
# : 내부 반복문 종료 여부를 변수로 저장 => 내부 반복문이 종료되면 외부 반복문이 함께 종료

#내부 반복문 종료 여부 변수로 설정
isbreak=False

for d in range(2,10):
    print(f'\n[{d}단]',end=' ')
    for n in range(1,10):
        print(f'{d}*{n}={d*n:<2}',end=' ')
        if n==d:
            isbreak=True   
            break
    if isbreak: break