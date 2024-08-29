#-----
#set 자료형: 여러 가지 종류의 여러 개 데이터 저장
# 중복 X
# 컬렉션 타입의 데이터 저장 시 tuple 가능
# {데이터1, 데이터2, ...., 데이터n}
#-----
#set 생성
data=set()  #빈 set
print(f'data의 타입: {type(data)}, 원소/요소 개수:{len(data)}개, 데이터: {data}')

#여러 개의 데이터를 저장한 set
data={10,30,20,-9,10,30,10,30,10,10}
print(f'data의 타입: {type(data)}, 원소/요소 개수:{len(data)}개, 데이터: {data}')
#여러 종류의 데이터를 저장한 set
data={9.34,'apple',10,True,'10'}
print(f'data의 타입: {type(data)}, 원소/요소 개수:{len(data)}개, 데이터: {data}')

# data={1,2,3,[1,2,3]}
print(f'data의 타입: {type(data)}, 원소/요소 개수:{len(data)}개, 데이터: {data}')

data={1,2,3,(1,2,3)}
print(f'data의 타입: {type(data)}, 원소/요소 개수:{len(data)}개, 데이터: {data}')

data={1,2,3,(1,)[0]}
print(f'data의 타입: {type(data)}, 원소/요소 개수:{len(data)}개, 데이터: {data}')

# data2={1,2,3, {1:100}}
print(f'data의 타입: {type(data)}, 원소/요소 개수:{len(data)}개, 데이터: {data}')

#set() 내장함수
data={1,2,3} #=set([1,2,3])
data=set() #empty set
data=set({1,2,3})
data=set([1,2,1,2,3])

data=set('good')
print(data)

data=list('good')
print(data)

data=set({'name':'홍길동', 'age':12,'name':'베트맨'})  #set
print(data)

print({'name':'홍길동', 'age':12,'name':'베트맨'})  #dict

data=set((1,2,1,2,1))
print(data)