#-----
#tuple 데이터: 다양한 종류의 여러 개 데이터 저장, 수정·삭제 안 됨
# 형식: (데1,..,데n)
#        데1,...,데n
#       (데1,)or 데1,      
#-----
datas=()
print(type(datas), datas,len(datas))

datas=(1,5,7)
print(type(datas), datas,len(datas))

# datas=(1)
# print(type(datas), datas,len(datas))

datas=(1,)
print(type(datas), datas,len(datas))

datas=1,
print(type(datas), datas,len(datas))

#tuple 데이터의 원소/요소 읽기
datas=11,22,33,44,55
print(datas[2], datas[-3])
print(datas[1:4])

#tuple 데이터 수정, 삭제: 불가
datas=11,22,33,44,55
datas[-1]='A'
del datas[-1]

#tuple 데이터의 원소/요소 변경: 형변환 필요
b_day=(2024,1,1)
#1월 -> 3월 변경
b_day=list(b_day)  #tuple -> list
b_day[1]=3
b_day=tuple(b_day)  # list -> tuple
