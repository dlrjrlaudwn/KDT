#--------
#내장함수 map()
# map(함수명, 데이터)  ex) map(int, )
#--------

data=input('숫자 데이터 입력 : ')
print(type(data), data)
nums=data.split()  #split: 한개의 문자열이 여러개로 분리

# 문자열 숫자 => 정수로 형변환
result=map(int, nums)
print(type(result), result)

#------
#형변환
#------
a=10
b=3
print(a/b)  #나머지가 생기니까 자동 형변환으로 int -> float


