#-----
#글자를 입력받고 입력받은 글자의 코드값 출력
#-----
msg=input('글자 입력(a~z, A~Z):')
if len(msg)>0:
    if len(msg)==1:
        if 'a'<=msg<='Z'or'A'<=msg<='Z':
            print(f'{msg}의 코드값: {ord('msg')}')
        else:
            print('알파벳 대,소문자만 가능합니다.')
    else:
        print('1개의 문자만 입력하세요.')

else:
    print('입력된 데이터가 없습니다.')


if len(msg) and ('a'<=msg<='Z'or'A'<=msg<='Z'):
    print(f'{msg}의 코드값: {ord('msg')}')
else:
    print('1개의 알파벳 문자만 입력해야 합니다.\n입력된 데이터를 확인하세요.')

data='Ab'
print(list(map(ord,data)))

#점수를 입력 받아서 학점 출력(A+~F)
# A+: 96~100
# A: 95
# A-:90~94
score=input('점수:')
if 96<=score<=100:
    print('A+')
elif score==95:
    print('A')
elif 90<=score<=94:
    print('A-')
elif 86<=score<=89:
    print('B+')
elif score==85:
    print('B')
elif 80<=score<=84:
    print('B-')
elif 76<=score<=79:
    print('C+')
elif score==75:
    print('C')
elif 70<=score<=74:
    print('C-')
elif 66<=score<=69:
    print('D+')
elif score==65:
    print('D')
elif 60<=score<=64:
    print('D-')
else:
    print('F')

score=00
grade=''
if score<0 or score>100:
    print(f'{score}는 잘못 입력된 점수입니다.')
else:
    if score>95: grade='A+'
    elif score==95: grade='A'
    elif score>=90: grade='A-'
    .
    .
    .
    else: grade='f'
    print(f'{score}는 {grade} 학점입니다.')

