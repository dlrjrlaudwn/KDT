#081
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score,_,_=scores
print(valid_score)

#082
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,_,*valid_score=scores
print(valid_score)

#083
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,*valid_score,_=scores
print(valid_score)

#084
temp={}

#085
x={'메로나':1000,'폴라포':1200,'빵빠레':1800}
print(x)

#086
x={'메로나':1000,'폴라포':1200,'빵빠레':1800}
x['죠스바']=1200
x['월드콘']=1500
print(x)

#087
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print('메로나 가격:', ice['메로나'])

#088
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice['메로나']=1300

#089
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
del ice['메로나']

#090
# >> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# >> icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'
#딕서녀리에 '누가바'가 없음

#091
inventory={'메로나':[300,20],'비비빅':[400,3],'죠스바':[250,100]}

#092
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print(inventory['메로나'][0],'원')

#093
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print(inventory['메로나'][1],'개')

#094
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
inventory['월드콘']=[500,7]
print(inventory)

#095
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
key=list(icecream.keys())

#096
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
value=list(icecream.values())

#097
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(sum(icecream.values()))

#098
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)

#099
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result=dict(zip(keys,vals))

#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table=dict(zip(date,close_price))

#101
#bool 타입

#102
print(3 == 5)
#False

#103
print(3 < 5)
#True

#104
x = 4
print(1 < x < 5)
#True

#105
print ((3 == 3) and (4 != 3))
#True

#106
#print(3 => 4)
# >= 이렇게 써야 함

#107
if 4 < 3:
    print("Hello World")
#False라서 출력 X

#108
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
#Hi, there.

#109
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
#1
#2
#4

#110
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
#3
#5

#111
x=input()
print(x*2)

#112
x=input()
print(int(x)+10)

#113
x=input()
if int(x)%2:
    print('홀수')
else:
    print('짝수')

#114
x=input()
if int(x)+20<=255:
    print(int(x)+20)
else:
    print('255')

#115
x=input()
if 0<int(x)-20<=255:
    print(int(x)-20)
elif int(x)-20<0:
    print('0')
else:
    print('225')

#116
x=input()
if x[-2:]=='00':
    print('정각입니다')
else:
    print('정각이 아닙니다')

#117
fruit = ["사과", "포도", "홍시"]
x=input()
if x in fruit:
    print('정답입니다')
else:
    print('오답입니다')

#118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
x=input()
if x in warn_investment_list:
    print('투자 경고 종목입니다')
else:
    print('투자 경고 종목이 아닙니다')

#119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
x=input()
if x in fruit:
    print('정답입니다')
else:
    print('오답입니다')

#120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

x=input()
if x in fruit.values():
    print('정답입니다')
else:
    print('오답입니다')

#121
x=input()
if x.islower():
    print(x.upper())
else:
    print(x.lower())

#122
score=int(input())
if 81<=score<=100:
    print('grade is A')
elif 61<=score<=80:
    print('grade is B')
elif 41<=score<=60:
    print('grade is C')
elif 21<=score<=40:
    print('grade is D')
else:
    print('grade is E')

#123

#124
num1=input('input number1: ')
num2=input('input number2: ')
num3=input('input number3: ')
if num1>=num2 and num1>=num3:
    print(num1)
elif num2>=num1 and num2>=num3:
    print(num2)
else:
    print(num3)

#125
x=input().split('-')[0]
if x=='011':
    print('당신은 skt 사용자입니다.')
elif x=='016':
    print('당신은 kt 사용자입니다.')
elif x=='019':
    print('당신은 lgu 사용자입니다.')
else:
    print('당신은 알수없음 사용자입니다.')

#126
x=input('우편번호:')
if x[2] in ['0','1','2']:
    print('강북구')
elif x[2] in ['3','4','5']:
    print('도봉구')
else:
    print('노원구')

#127
x=input('주민등록번호:').split('-')[1]
if x[0]=='1' or x[0]=='3':
    print('남자')
else:
    print('여자')

#128
x=input('주민등록번호:').split('-')[1]
if 0<=int(x[1:3])<=8:
    print('서울입니다')
else:
    print('서울이 아닙니다')

#129
x=input('주민등록번호:').split('-')
x1=int(x[0])
x2=int(x[1])

result1= 

result2=str(11-(result1%11))

if result2==x[-1]:
    print('유효한 주민등록번호입니다.')
else:
    print('유효하지 않은 주민등록번호입니다.')

#130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# 변동폭=(max_price)-(min_price)
# 시가=(opening_price)
# 최고가=(max_price)
if (시가+변동폭)>최고가:
    print('상승장')
else:
    print('하락장')

#131
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)
# 사과
# 귤
# 수박

#132
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")
# #####
# #####
# #####

#133
for 변수 in ["A", "B", "C"]:
  print(변수)

변수="A"
print(변수)
변수="B"
print(변수)
변수="C"
print(변수)

#134
for 변수 in ["A", "B", "C"]:
  print("출력:", 변수)

변수="A"
print("출력:",변수)
변수="B"
print("출력:", 변수)
변수="C"
print("출력:", 변수)

#135
for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환:", b)

변수="A"
b=변수.lower()
print("변환:", b)
변수="B"
b=변수.lower()
print("변환:", b)
변수="C"
b=변수.lower()
print("변환:", b)

#136
for 변수 in [10,20,30]:
    print(변수)

#137
for a in [10,20,30]:
    print(a)

#138
for a in [10,20,30]:
    print(a)
    print('-------')

#139
print("++++")
for a in [10,20,30]:
    print(a)

#140
for a in [1,2,3,4]:
    print('-------')

#141
리스트 = [100, 200, 300]
for a in 리스트:
    print(a+10)

#142
리스트 = ["김밥", "라면", "튀김"]
for a in 리스트:
    print('오늘의 메뉴:',a)

#143
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for a in 리스트:
    
#144
리스트 = ['dog', 'cat', 'parrot']
for a in 리스트:
    print(a, len(a))

#145
리스트 = ['dog', 'cat', 'parrot']
for a in 리스트:
    print(a[0])

#146
리스트 = [1, 2, 3]
for a in 리스트:
    print('3 x',a)

#147
리스트 = [1, 2, 3]
for a in 리스트:
    print(f'3 x {a} = {3*a}')

#148
리스트 = ["가", "나", "다", "라"]

for a in 리스트[1:]:
  print(a)

#149
리스트 = ["가", "나", "다", "라"]

for a in 리스트[::2]:
  print(a)

#150
리스트 = ["가", "나", "다", "라"]

for a in 리스트[::-1]:
  print(a)

#151
리스트 = [3, -20, -3, 44]

for a in 리스트:
  if a<0: print(a)

#152
리스트 = [3, 100, 23, 44]

for a in 리스트:
  if a%3==0: print(a)

#153
리스트 = [13, 21, 12, 14, 30, 18]

for a in 리스트:
  if a<20 and a%3==0: print(a)

#154
리스트 = ["I", "study", "python", "language", "!"]

for a in 리스트:
  if len(a)>=3: print(a)

#155
리스트 = ["A", "b", "c", "D"]

for a in 리스트:
  if a.isupper(): print(a)

#156
리스트 = ["A", "b", "c", "D"]

for a in 리스트:
  if a.isupper()==False: print(a)

#157
리스트 = ['dog', 'cat', 'parrot']

for a in 리스트:
  print(a[0].upper()+a[1:])

#158
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']

for a in 리스트:
  a=a.split('.')
  print(a[0])

#159
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for a in 리스트:
  b=a.split('.')
  if b[1]=='h': print(a)

#160
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for a in 리스트:
  b=a.split('.')
  if b[1]=='h'or b[1]=='c': print(a)

#161
for a in range(100): print(a)

#162
for a in range(2002,2051,4):
  print(a)

#163
for a in range(3,31,3):
  print(a)

#164 ????????????
for a in range(100,-1):
  print(a)

#165
for a in range(10):
  print(f'0.{a}')

#166
for a in range(1,10):
  print(f'{3}X{a} = {3*a}')

#167
for a in range(1,10):
  if a%2!=0:
    print(f'{3}X{a} = {3*a}')

#168
b=0
for a in range(1,11):
  b=b+a
print('합:',b)

#169
b=0
for a in range(1,11,2):
  b=b+a
print('합:',b)

#170
b=1
for a in range(1,11):
  b=b*a
print(b)

#171
price_list = [32100, 32150, 32000, 32500]

for a in range(4):
  print(price_list[a])

#172
price_list = [32100, 32150, 32000, 32500]

for a in range(len(price_list)):
  print(a, price_list[a])

#173
price_list = [32100, 32150, 32000, 32500]

for a in range(len(price_list)):
  print((len(price_list)-1)-a,price_list[a])

#174
price_list = [32100, 32150, 32000, 32500]

for a in range(1,4):
  print(10*a+90,price_list[a])

#175
my_list = ["가", "나", "다", "라"]

for a in range(3):
  print(my_list[a],my_list[a+1])


#176
my_list = ["가", "나", "다", "라", "마"]

for a in range(3):
  print(my_list[a],my_list[a+1],my_list[a+2])

#177
my_list = ["가", "나", "다", "라"]

for a in range(3):
  print(my_list[3-a],my_list[2-a])

#178
my_list = [100, 200, 400, 800]

for a in range(3):
  print(my_list[a+1]-my_list[a])

#179
my_list = [100, 200, 400, 800, 1000, 1300]

for a in range(1,5):
  print((my_list[a-1]+my_list[a]+my_list[a+1])/3)


#180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility=[]
for a in range(len(low_prices)):
  volatility.append([high_prices[a]-low_prices[a]])
