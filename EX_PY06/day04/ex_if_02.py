#-----
#숫자를 입력받아서 음이 아닌 정수/음수 구분하기
#-----
num=int(input('숫자:'))

if num>=0:
    print(f'숫자 {num}은 음이 아닌 정수입니다')
else:
    print(f'숫자 {num}은 음수입니다.')

#-----
#점수를 입력받아서 합격/불합격 구분하기
# 합격: 60점 이상
#-----
num=int(input('점수:'))

if num>=60:
    print(f'{num}점은 합격입니다')
else:
    print(f'{num}은 불합격입니다.')

#-----
#점수를 입력받아서 학점 구분하기
# 학점: A,B,C,D,F
#-----
num=int(input('점수:'))

if num>=90:
    print(f'{num}점은 A 학점입니다')
elif num<90 and num>=80:
    print(f'{num}점은 B 학점입니다')
elif num<80 and num>=70:
    print(f'{num}점은 C 학점입니다')
elif num<70 and num>=60:
    print(f'{num}점은 D 학점입니다')
else:
    print(f'{num}점은 F 학점입니다')