# while문으로 3단 출력
n=1
while n<10:
    print(f'{3}*{n}={3*n}')
    n=n+1

#1~30 범위의 수 중에서 홀수만 출력
# 1) 1~30 출력
n=1
while n<31:
    print(n)
    n=n+1
# 2) 홀수 출력
n=1
while n<31:
    if n%2:
        print(n)
    n=n+1
n=1
while n<31:
    print(n)
    n=n+2