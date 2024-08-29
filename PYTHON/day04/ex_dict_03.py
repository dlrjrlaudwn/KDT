#-----
#dict 자료형 전용 함수(메서드 Method) 사용
# 변수명.메서드명()
#-----
# dict에서 key만 추출: keys()
p1={'name':'홍길동','age':20, 'job':'학생'}

result=p1.keys()
print(f'키 추출:{result}, {type(result)}')

# print(result[0])

#list 형변환해서 key 저장해야 함: list(dict_keys타입)
result=list(result)
print(f'키 추출:{result}, {type(result)}')

# dict에서 value만 추출: values()
result=p1.values()
print(f'값 추출:{result}, {type(result)}')

# dict에서 key&value 추출: items()
result=p1.items()
print(f'키&값 추출:{result}, {type(result)}')

#list로 형변환
result=list(result)
print(f'키&값 추출:{result[0]}, {type(result[0])}')
