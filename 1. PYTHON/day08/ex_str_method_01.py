#-----
#str 데이터 타입 전용 함수(메서드)
#-----
msg='hello 0705'
#원소/요소 인덱스 찾기 메서드 1: find(문자 1개/문자열)
# 'h' 인덱스 찾기
idx=msg.find('h')
print(f'h의 인덱스:{idx}')

idx=msg.find('7')
print(f'7의 인덱스:{idx}')

idx=msg.find('llo')  #llo의 시작 위치 알려줌
print(f'llo의 인덱스:{idx}')

idx=msg.find('llO')  # 대소문자 일치해야 함/존재하지 않으면(일치하지 않으면) -1 결과로 줌
print(f'llO의 인덱스:{idx}')

#원소/요소의 인덱스 찾기 메서드 2: index(문자 1개/문자열)
idx=msg.index('h')
print(f'h의 인덱스:{idx}')

if 'H' in msg:
    idx=msg.index('H')
    print(f'H의 인덱스:{idx}')
else: print('H는 존재하지 않습니다.')

#문자열에 동일한 문자가 여러개 존재하는 경우
msg='good luck good'

# 첫번째 'o'의 인덱스 찾기
idx=msg.find('o')
print(f'첫번째 o의 인덱스: {idx}')

# 두번째 'o'의 인덱스 찾기
idx=msg.find('o',idx+1)
print(f'두번째 o의 인덱스: {idx}')

# 세번째 'o'의 인덱스 찾기
idx=msg.find('o',idx+1)
print(f'세번째 o의 인덱스: {idx}')

# 네번째 'o'의 인덱스 찾기
idx=msg.find('o',idx+1)
print(f'네번째 o의 인덱스: {idx}')

#이걸 반복문으로 하면
cnt=msg.count('o')
print(f'cnt: {cnt}')
idx=-1
for n in range(cnt):
    idx=msg.find('o',idx+1)
    print(f'{n+1}번째 o의 인덱스: {idx}')

#문자열의 뒷부분부터 찾기: rfind(찾을 문자, 시작 인덱스, 끝 인덱스+1),rindex()
msg='happy'
# y인덱스 찾기
idx=msg.rfind('y')
print(idx)

# 첫번째 p인덱스 찾기
idx=msg.rfind('p')
print(idx)

# 두번째 p인덱스 찾기
idx=msg.rfind('p',0,idx)  #0 ~ (idx-1) 구간에서 p 찾기
print(idx)

# 파일명에서 확장자(txt, jpeg, xlsx, zip ...) 찾기
files=['hello.txt','2024상반기경제분석.doc','kaka_1316532.jpg']
for file in files:
    data=file.rfind('.')
    print(file[data+1:])

