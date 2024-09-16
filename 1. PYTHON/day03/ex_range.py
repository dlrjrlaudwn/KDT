#-----
#내장함수 range: 숫자 범위를 생성하는 내장함수
# 형식: range(시작숫자, 끝숫자+1, 간격)
#       range(끝숫자+1) => 첨부터 끝숫자+1까지 1 간격
#-----

#1~100까지 저장
nums=range(1,101)
print(f'nums 값: {nums}\n타입: {type(nums)}\n개수: {len(nums)}')

#원소/요소 읽기: 인덱싱
print(nums[0], nums[-1])

#원소/요소 여러 개 읽기: 슬라이싱
print(nums[0:10], nums[30:41])

#원소/요소 하나씩 보기: list/tuple 형변환
print(list(nums[0:10]), tuple(nums[30:41]))

#-----
#1~100에서 3의 배수만 저장: 3,6,..,99
three=range(3,101,3)
print(list(three))

#1.0~10.0사이에 숫자 저장
# range(1.0, 10.1)

datas=list(range(1,11))
print(datas)
datas=list(map(float,datas))
print(datas)
