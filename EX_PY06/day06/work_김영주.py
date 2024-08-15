#구구단을 for문 1개로 출력


#구구단 전체 가로 출력
for n in range(1,10):
  for d in range(2,6):
    print(f'{d}*{n}={d*n:>2}', end='\t')
    if d==5:
      print()
print('\n')
for n in range(1,10):
  for d in range(6,10):
    print(f'{d}*{n}={d*n:>2}', end='\t')
    if d==9:
      print()

#17.5 연습문제
i=2
j=5
while i<=32 or j>=1:
  print(i,j)
  i=i*2
  j=j-1

#17.6 심사문제
data=int(input())-1350
while data>=0:
  print(data)
  data=data-1350

#18.5 연습문제
i=0
while True:
  if i>73:
    break
  if i%10!=3:
    i=i+1
    continue
  print(i, end=' ')
  i+=1

#18.6 심사문제
start,stop=map(int,input().split())
i=start
while True:
  if i%10==3:
    i=i+1
    continue
  if i>stop:
    break
  print(i,end=' ')
  i+=1

#19.5 연습문제
for i in range(5):
  for j in range(5):
    if j<i:
      print(' ',end='')
    else:print('*',end='')
  print()

#19.6 심사문제 ????????????????
i=int(input())
for i in range(i):
  for j in range(i*2-1):
    if j-1<=i-1<=j+1:
      print('*',end='')
    else: print(' ',end='')
  print()

#20.7 연습문제
for i in range(1,101):
  if (i%2==0) and (i%11==0):
    print('FizzBuzz')
  elif i%2==0:
    print('Fizz')
  elif i%11==0:
    print('Buzz')
  else:
    print(i)

#20.8 심사문제
start,stop=map(int,input().split())
for i in range(start,stop+1):
  if i%5==0 and i%7==0: print('FizzBuzz')
  elif i%5==0: print('Fizz')
  elif i%7==0: print('Buzz')
  else: print(i)