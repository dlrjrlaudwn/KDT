#-----
#연산자와 내장함수
#-----
person={'name':'홍길동','age':20, 'job':'학생'}
dog={'kind':'말티즈', 'weight':'2kg', 'color':'white','gender':'남', 'age':10}

#연산자
#산술 연산 X
# person+dog
#멤버 연산 O
print('name'in dog)
print('name'in person)
#value는 멤버 연산 X
print('허스키'in dog)
print(20 in person)

#value 추출
print('말티즈'in dog.values())

#내장함수
# 원소/요소 개수 확인: len()
print(f'dog의 요소 개수:{len(dog)}개')
print(f'person의 요소 개수:{len(person)}개')

# 원소/요소 정렬: sorted() <- key만 정렬
print(f'dog 정렬:{sorted(dog)}')
print(f'dog 정렬:{sorted(dog,reverse=True)}')
#value 정렬
# print(f'dog 정렬:{sorted(dog.values())}')

#------
jumsu={'국어':90, '수학':178, '체육':100}
print(f'jumsu 값 정렬:{sorted(jumsu.values())}')
print(f'jumsu 값 정렬:{sorted(jumsu)}')

#키&값 묶어서 정렬 => 기본: 키 기준 정렬
print(f'jumsu 값 정렬:{sorted(jumsu.items())}')
#값 기준 정렬
print(f'jumsu 값 정렬:{sorted(jumsu.items(),key=lambda x:x[1])}')
