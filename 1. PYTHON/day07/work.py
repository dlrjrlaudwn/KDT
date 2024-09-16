#18.5 연습문제
i=0
while True:
    if i>73: break
    if i%10!=3:
        i=i+1
        continue
    print('i',end=' ')
    i=i+1