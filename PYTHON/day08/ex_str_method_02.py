#문자열에서 좌우 여백 제거 메서드: strip(), lstrip(),rstrip()
# 문자열 내부 공백은 제거 X
msg='good luck'
data=' happy new year 2025!  '

#좌우 모든 공백 제거
m1=msg.strip() #복사본 형태로 출력 => 저장 필요
print(f'원본 msg:{len(msg)}개 --- 제거 m1:{len(m1)}개')

d1=data.strip()
print(f'원본 data:{len(data)}개 --- 제거 da:{len(d1)}개')

# 왼쪽(문자열 시작 부분) 공백 제거
d1=data.lstrip()
print(f'원본 data:{len(data)}개 --- 제거 da:{len(d1)}개')

# 오른쪽(문자열 끝 부분) 공백 제거
d1=data.rstrip()
print(f'원본 data:{len(data)}개 --- 제거 da:{len(d1)}개')

#이름을 입력받아서 저장
name=input('이름:').strip()
if len(name)>0:
    print(f'name:{name}')
else: print('입력하지 않았습니다.')

#입력받은 데이터에 따라 다른 출력(알파벳 => ★ / 숫자 => ♥ / 나머지 => 무시)
data=input('1개 입력:').strip()   #입력 시 공백을 입력하면 공백은 제거하고 조건문 진행하고자 strip()
if 'a'<=data<='z' or 'A'<=data<='Z': print('★') 
elif '0'<=data<='9': print('♥')
