#-----
#문자열 str 데이터 다루기
#-----
#여러 줄 문자열 => msg='''~~~~''' or """~~~"""  cf) msg= 없으면 주석되버림
msg='''
오늘은 

좋은날
기쁜날

'''

print(f'msg => {msg}')

#인덱싱: 문자열 안에 문자 한개씩 식별하는 방법
# 원소/요소: 문자열 안에 문자 1개
# 변수명[인덱스], 문자열데이터[인덱스]
# 방법: (왼 -> 오) 0, 1 ...
#       (왼 <- 오) ...-2, -1
msg='good luck!'

print(msg)
print(msg[0])
print(msg[4])
print(msg[-1])

# msg2=''
# print(msg2[0])

#원소/요소의 개수 파악해주는 내장 함수 len()
# 원소/요소를 갖고 있는 데이터 타입에만 사용 가능
msg='good luck!'
print(len(msg))

#제일 마지막 원소/요소만 출력
msg='good'
print(msg[3], msg[len(msg)-1], msg[-1])

#-----
#슬라이싱: 문자열 내에 연속된 요소/원소 추출
# 변수명[시작:끝+1]
#-----
data='happy new year 2025! good luck'
print(f'인덱스 범위: 0 ~ {len(data)-1}')
print(data[15:20])

a='life is too short, you need python'
print(a[0:4], a[:4])
print(a[19:35], a[19:])
print(a[:])

#-----
#슬라이싱: 문자열 내에 규칙/패턴을 가진 요소/원소 추출
# 변수명[시작:끝+1:간격]
#-----
data='123456789'

#2.4.6.8 추출
print(data[1], data[3], data[5], data[7])
print(data[1:8:2])
print(data[1: :2])

data='ABC1DEF2GHI3JKL4MNO5PQR6STU'
#문자열에 숫자 요소만 추출
print(data[3: :4])
print(data[3:-1:4])
print(data[3:len(data):4])

