#-----
#이스케이프 문자: 특수한 의미를 가지는 문자
# 형식: \문자  
# '\n': 줄바꿈
# '\t': 탭간격
# '\'': 홑따옴표 문자
# '\"': 쌍따옴표 문자
# '\\': 백슬러시 문자(주로 경로(path), URL 관련)
# '\U': 유니코드
# '\a': 알람소리 ...
#-----

msg='오늘은 좋은 날\n내일은 주말이라 행복해'
print(F'msg 줄바꿈: {msg}')

msg='오늘은 나의 \'생일\'이야'
print(msg)

file='C:\\Users\\desktop\\Saved Games\\test.txt'
print(file)

# r''/R'': 문자열 내 이스케이프 문자는 무시됨
file=r'C:\Users\desktop\Saved Games\test.txt'
print(file)

msg='happy\tnew\tyear'
msg2=r'happy\tnew\tyear'
print(msg, msg2)

