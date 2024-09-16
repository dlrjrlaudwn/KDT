#-----
#요소 순서 제어 메서드: reverse()
#-----
import random as rad

rad.seed(10) #동일한 랜덤 숫자 추출을 위한 기준

datas=[]
for _ in range(10):
    datas.append(rad.randint(1,30))

print(f'{len(datas)}개, {datas}')

# datas 좌우반전
datas.reverse()
print(f'{len(datas)}개, {datas}')

#요소 별 크기 비교&정렬 메서드: sort()
# 기본 정렬: 오름차순
datas.sort()
print(f'{len(datas)}개, {datas}')
#내림차순
datas.sort(reverse=True)
print(f'{len(datas)}개, {datas}')

#리스트에서 요소를 꺼내는 메서드: pop()
# 실행 시,리스트에서 삭제됨
# remove는 지우는 거고 pop은 꺼내서 활용 가능
value=datas.pop()
print(f'value: {value}-{len(datas)}개, {datas}')

#특정 인덱스의 원소/요소 꺼내기
value=datas.pop(0)
print(f'value: {value}-{len(datas)}개, {datas}')

#리스트 확장 메서드: extend()
datas.extend([11,22,33])
print(f'{len(datas)}개, {datas}')

datas.extend((555,777))
print(f'{len(datas)}개, {datas}')

datas.extend('good luck')
print(f'{len(datas)}개, {datas}')

datas.extend({555,777,555,777})
print(f'{len(datas)}개, {datas}')

datas.extend({'name':'홍길동','age':12})
print(f'{len(datas)}개, {datas}')

#모든 원소 삭제 메서드: clear()
datas.clear()
print(f'{len(datas)}개, {datas}')
