#-----
#반복문 중단 break문: 반복을 중단시키는 조건문과 함께 사용
#-----
#숫자 데이터(1~50)의 합계가 30 이상이 되면 더이상 합계 X
nums=range(1,51)
total=0
for n in nums:
    if total>=30:
        break          #즉시 반복 종료
    total=total+n

print(f'total:{total} {1}~{n-1}까지의 합계')

#-----
#4개 과목점수 중 각 과목 점수가 40점 이하&평균 60점 이하: 불합격
score=[89,39,80,77]
ispass=True
#과락 확인
for n in score:
    if n<40:
        print('과락입니다.')
        ispass=False
        break
#합/불 확인
if ispass:
    avg=sum(score)/len(score)
    if avg>=60:
        print(f'{avg}점으로 합격입니다.')
    else: print(f'{avg}점으로 불합격입니다.')
else: print(f'과락으로 불합격 입니다.')

score=[89,41,80,77]
ispass=True            #flag 변수
#과락 확인
for n in score:
    if n<40:
        print('과락입니다.')
        ispass=False
        break
#합/불 확인
if ispass:
    avg=sum(score)/len(score)
    if avg>=60:
        print(f'{avg}점으로 합격입니다.')
    else: print(f'{avg}점으로 불합격입니다.')
else: print(f'과락으로 불합격 입니다.')

