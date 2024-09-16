#ㄱㅖ산기 만들기
#사칙연산 기능별 함수 생성(+ - * /), 2개의 정수만 계산

def plus(num1,num2):
    return num1+num2

def minus(num1,num2):
    return num1-num2

def mult(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2 if num2 else '0으로 나눌 수 없음'

#기능:연산 수행 후 결과 반환
#이름: calc
#매개변수: 함수명, str 숫자 2개, 연산자 기호
#결과: 없음
def calc(func,num1,num2, op):
    data=input('정수 2개:')
    if check_data(data,2):
        print(f'결과:{data[0]}{op}{data[1]}={func(int(data[0]),int(data[1]))}')
    else: print(f'{data}:올바른 데이터가 아닙니다.')

#기능: 입력 받은 데이터가 유효한 데이터인지 검사
#이름: check_data
#매개변수: str 데이터(ex_10 3), 데이터 수
#결과:True/False
def check_data(data,count):
    #입력된 문자열을 리스트로 바꾸기:split
    data=data.split()
    #개수 확인
    if len(data)==count:
        #숫자인지 확인
        isok=True
        for d in data:
            if not d.isdecimal():
               isok=False
               break
        return isok
    else: return False   
    
#메뉴 출력 함수
#기능: 계산기 메뉴 출력
#이름: print_menu
#매개변수: 없음
#결과: 없음
def print_menu():
    print(f'{"*":*^16}')   #"(데이터)":*(빈칸은 *로 채우기) ^(가운데 정렬)16(16칸)
    print(f'{"계산기":^16}')
    print(f'{"*":*^16}')
    print(f'{"* 1 덧      셈 *":16}')
    print(f'{"* 2 뺄      셈 *":16}')
    print(f'{"* 3 곱      셈 *":16}')
    print(f'{"* 4 나  눗  셈 *":16}')
    print(f'{"* 5 종      료 *":16}')
    print(f'{"*":*^16}')

print_menu()

#사용자에게 원하는 계산을 선택하는 메뉴 출력/종료 메뉴 선택 시 프로그램 종료
# => 무한 반복: while

while True:
    #메뉴 출력
    print_menu()
    #메뉴 선택 요청
    choice=input('메뉴 선택:')
    if choice.isdecimal():
        choice=int(choice)
    else:
        print('0~9 사이 숫자만 입력하세요')
        continue
    #종료 조건(5번 선택) 처리
    if choice==5:
        print('프로그램을 종료합니다.')
        break
    elif choice==1:
        print('덧셈')
        num1,num2=input('정수 2개:').split()
        num1=int(num1)
        num2=int(num2)
        print(f'{num1}+{num2}={num1+num2}')
    elif choice==2:
        print('뺄셈')
        num1,num2=input('정수 2개:').split()
        calc(minus,num1,num2,'-')
    elif choice==3:
        print('곱셈')
        num1,num2=input('정수 2개:').split()
        calc(mult,num1,num2,'*')
    elif choice==4:
        print('나눗셈')
        num1,num2=input('정수 2개:').split()
        calc(div,num1,num2,'/')
    else: print('선택된 메뉴가 없습니다')
