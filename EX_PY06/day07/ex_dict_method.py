#-----
#dict 메서드: keys(),values(),items()
#-----
person={'name':'홍길동','age':10}

#key로 value 읽어오는 메서드: get(key)
print(person['name'])
#print(person['gender'])

print(person.get('name'))
print(person.get('gender','없음'))
print(person.get('gender'))

#dict에 key-value 추가: setdefault(k,v)
person['gender']='남'

msg='hello good luck'
#알파벳 개수별로 몇갠지
alpha=set(msg)
save={}
for m in alpha:
    print(m,msg.count(m))
    save[m]=msg.count(m)
print(save)


for m in msg:
    print(m,msg.count(m))

#수정/업데이트: update(k=v)
person['gender']='여'

person.update(gender='어린이',job='학생')
print(person)

person.update({'phone':'010','birth':'240101'})
print(person)

person.update(**{'weight':'100','height':'170'})
print(person)