#-----
#요소 추가 메서드: append()
# 제일 마지막 원소로 추가됨
#-----
datas=[1,3,5]

#새로운 데이터 추가
datas.append(100)
print(f'datas의 개수: {len(datas)}, {datas}')

datas.append(100)
print(f'datas의 개수: {len(datas)}, {datas}')

#원하는 위치에 요소 추가 메서드: insert()
datas.insert(0,300)
print(f'datas의 개수: {len(datas)},{datas}')

datas.insert(-1,300)
print(f'datas의 개수: {len(datas)},{datas}')

#임의의 정수 10개를 저장하는 리스트 생성
import random as rad
datas=[]
for cnt in range(10):
    datas.append(rad.randint(1,50))
print(f'datas: {datas}')

#요소 삭제 메서드: remove()
datas=[300, 1, 3, 5, 100, 300, 100]
datas.remove(300)
print(datas)
datas.remove(300)
print(datas)
#datas.remove(300)
print(datas)

for cnt in range(datas.count(300)):
    datas.remove(300)
    print(datas)