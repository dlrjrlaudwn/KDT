#1
for i in range(5):
    for j in range(5):
        print(f'j:{j}, end=' '')
    print(f'i:{i}\\n')

#대각선으로 * 출력하기
for v in range(5):
    for h in range(v+1):
        if v==h:
            print('*')
        else: 
            print(' ',end='')

for v in range(5):
    for h in range(v+1):
        print('*' if h==v else ' ',end='\n' if h==v else '')