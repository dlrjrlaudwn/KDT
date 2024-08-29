#-----
#임의의 숫자가 5의 배수인지 아닌지 결과 출력
#-----
num=209
print('5의 배수가 아닙니다.') if num%5 else print('5의 배수입니다.')

#문자열을 입력받아서 문자열의 원소 개수 저장(원소 개수가 0이면 None 저장)
msg=input()
result=len(msg) if len(msg)>0 else None
result=len(msg) if len(msg) else None #len(msg)에 값이 있으면 True => len(msg) 저장함
print(result)

#연산자와 숫자 2개를 입력 받아서 입력된 연산자에 따라 계산 결과 저장
# ex) 입력: + 10 3   출력: 13
data=input().split()
data1=int(data[1])
data2=int(data[2])
if data[0]=='+': result=data1+data2
elif data[0]=='-': result=data1-data2
elif data[0]=='*': result=data1*data2
elif data[0]=='/': result=data1/data2
else: print('사칙연산자가 아닙니다')
print(result)