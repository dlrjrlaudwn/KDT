#22.9 연습문제
a=['alpha','bravo','charlie','delta','echo','foxtrot','golf','hotel','india']
b=[i for i in a if len(i)==5]
print(b)

#22.10 심사문제
a,b=map(int,input().split())
c=[2**i for i in range(a,b+1)]
c.pop(1)
c.pop(-2)
print(c)

#25.7 연습문제
maria = {'korean':94,'english': 91,'mathematics':89,'science':83}

average=sum(maria.values())/len(maria)

print (average)