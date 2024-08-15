#-----
#문자열 str 데이터 다루기
# 문자요소 연산: 산술, 비교, 멤버 연산
#-----
#산술연산
data1='happy'
data2='year'

#덧셈 연산: str + str =strstr(연결)
print(f'{data1} + {data2} => {data1+data2}')
# print(f'{data1} + {10} => {data1+10}')
print(f'{data1} + {10} => {data1+str(10)}')

#뺄셈 연산: str - str = 미지원
# print(f'{data1} - {data2} => {data1-data2}')

#곱셈 연산: str * str = X
#          str * int = 숫자만큼 반복  
# print(f'{data1} * {data2} => {data1*data2}')
print(f'{data1} * {3} => {data1*3}')

#멤버 연산
#요소/원소 in 문자열 => 요소/원소가 문자열 안에 존재하면 T
#요소/원소 not in 문자열 => 요소/원소가 문자열 안에 없으면 T
data1='Happy'
print(f'h in {data1}:{"h" in data1}')
print(f'h not in {data1}:{"h" not in data1}')

#원소/요소를 가진 데이터 타입에서만 사용 가능
print(3 in 123)
print(len(123))
