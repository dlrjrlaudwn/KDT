"""
1 위치 먼저 지정

for문으로 2부터 끝까지 돌면서

count에 값 저장

row+1

col-1

if row,col 둘 다 벗어날 때 규칙

elif row 벗어날 때 규칙

elilf col 벗어날 때 규칙

count에 저장된 값들 프린트
"""

def magicsquare():
  n=int(input('홀수차 배열의 크기를 입력하세요: '))
  if n%2==0:
    print('짝수를 입력하였습니다. 다시 입력하세요')
    return magicsquare()
  print(f'Magic Square ({n}*{n})')

  rows=n
  cols=n
  matrix=[[0 for col in range(cols)]for row in range(rows)]

  matrix[0][n//2]=1
  y=0
  x=n//2

  for i in range(2, n*n+1):
    x=x+1
    y=y-1
    if x==n and y<0:
      y=y+2
      x=x-1
    elif y<0:
      y=n-1
    elif x>n-1:
      x=0
    elif matrix[y][x]!=0:
      x=x-1
      y=y+2

    matrix[y][x]=i

  for i in range(n):
    for j in range(n):
      print(f'{matrix[i][j]:3}', end=' ')
    print()


magicsquare()