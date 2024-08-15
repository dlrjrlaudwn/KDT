#12.4 연습문제
camille={'health':575.6, 'health_regen':1.7,'mana':338.8,'mana_regen':1.63,'melee':125,'attack_damage':60,'attack_speed':0.625,'armor':26,'magic_resistanc':32.1,'movement_speed':340}
print(camille['health'])
print(camille['movement_speed'])

#12.5 심사문제
lux=input().split()
num=(input().split())
dict=dict(zip(lux,num))
print(dict)

#13.6 연습문제
x=5
if x != 10:
    print('ok')

#13.7 심사문제
money=int(input())
coupon=(input())

if coupon=='Cash3000':
    print(money-3000)
if coupon=='Cash5000':
    print(money-5000)

#14.6 연습문제
written_test=75
coding_test=True

if written_test>=80 and coding_test==True:
    print('합격')
else:
    print('불합격')

#14.7 심사문제
korean,english,math,science=map(int,input().split())
if 0<=korean<=100 and 0<=english<=100 and 0<=math<=100 and 0<=science<=100:
    if (korean+english+math+science)/4 >=80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')

#15.3 연습문제
x=int(input())
if 11<=x<=20:
    print('11~20')
elif 21<=x<=30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')

#15.4 심사문제
age=int(input())
balance=9000
if 7<=age<12:
    balance=balance-650
elif 13<=age<=18:
    balance=balance-1050
elif age>=19:
    balance=balance-1250
print(balance)

