#-----
#리스트 전용의 함수, 메서드(method): 리스트의 원소/요소를 제어하기 위한 함수
#-----
import random as rad

datas=[18,4,10,2,9,13,95,99,1,3]

#요소 인덱스를 반환하는 메서드: index()
# 진행방향: 왼->오
# ex) 2의 인덱스 찾기
idx=datas.index(2)
print(f'2의 인덱스: {idx}')

# ex) 0의 인덱스 찾기
idx=datas.index(0)
print(f'0의 인덱스: {idx}')

if 0 in datas:
    idx=datas.index(0)
    print(f'0의 인덱스:{idx}')
else:
    print('존재하지 않는 데이터입니다.')

datas=[18,4,10,2,9,13,3,3,1,3]
if 3 in datas:
    idx=datas.index(3)
    print(f'3의 인덱스:{idx}')

# 존재하는 데이터의 개수 파악하는 메서드: count()
cnt=datas.count(3)
print(f'3의 개수: {cnt}개')
