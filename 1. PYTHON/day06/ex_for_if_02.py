#-----
#반복문&조건문 혼합
#-----
#입력받은 메시지에서 알파벳 대문자 -> 소문자, 소문자 -> 대문자, 나머지는 그대로 출력
msg=input()
for m in msg:
    if ('a'<=m<='z'):
        print(chr(ord(m)-32),end='')  #chr: 코드 -> 문자
    elif ('A'<=m<='Z'):
        print(chr(ord(m)+32),end='')
    else:
        print(m, end='')

