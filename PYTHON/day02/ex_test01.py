#---------
#입력/출력 실습
#---------
#1. 데이터 저장 및 변수 생성 및 출력
# 생년월일, 띠, 혈액형
# 출력형태: 나는 0000년 00월 00일 000띠 입니다.
#           혈액형은 _____ 0형 입니다.

year=1999
month=10
date=13
c_zodiac='토끼'
blood='A'
print(f'나는 {year}년 {month}월 {date}일 {c_zodiac}띠입니다')
print(f'혈액형은 소심한 {blood}형 입니다')


#2. 입력받은 데이터 파일로 저장
# 좋아하는 계절, 나라, 여행가고 싶은 나라

season=input('좋아하는 계절:')
nara=input('좋아하는 나라:')
nara2=input('가고싶은 나라:')

FILENAME='info.txt'
f=open(FILENAME, mode='w', encoding='utf-8')

#f.write(season)
#f.write('\n')  #줄바꿈 문자 추가해야 줄이 바뀜
#f.write(nara)
#f.write('\n')
#f.write(nara2)

print(f'좋아하는 계절:{season}', file=f)
print(f'좋아하는 나라: {nara}', file=f)
print(f'가고싶은 나라: {nara2}', file=f, end='')

f.close()
