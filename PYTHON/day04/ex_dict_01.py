#-----
#dict 자료형: 데이터의 의미를 함께 저장하는 자료형
# {key1:value, Key2:value,...}
# key: 중복 불가, value: 중복 가능
# 데이터 분석 시 파일 데이터를 가져올 때 많이 사용
#-----

#dict 생성
data={}
print(f'data => {len(data)}개, {type(data)}, {data}')

# ex1) 사람에 대한 정보 저장: 이름, 나이, 성별
data={'name':'마징가', 'age':100, 'gender':"남"}
print(f'data => {len(data)}개, {type(data)}, {data}')

# ex2) 강아지에 대한 정보: 품종, 무게, 색상, 성별, 나이
data={'kind':'말티즈', 'weight':'2kg', 'color':'white','gender':'남', 'age':10}
print(f'data => {len(data)}개, {type(data)}, {data}')

#dict 원소/요소 읽기
# 키를 가지고 값/데이터 읽음
# 형식: 변수명[키]
data={'kind':'말티즈', 'weight':'2kg', 'color':'white','gender':'남', 'age':10}

#색상
print(f'색상:{data["color"]}')

#성별, 품종
print(f'성별:{data["gender"]}, 품종:{data["kind"]}')

#dict 수정/변경
# 변수명[키]=새로운 값
#나이 10->11
data['age']=11
print(data)

#몸무게 2->3
data['weight']='3kg'
print(data)

#dict 삭제
# del 변수명[키]/del(변수명[키])
#성별 데이터 삭제
del data['gender']
print(data)

#dict 추가
# 변수명[새로운 키]=값
#이름 추가
data['name']='재롱이'
print(data)

data['name']='담비'
print(data)
