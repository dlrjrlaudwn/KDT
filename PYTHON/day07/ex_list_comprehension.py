#-----
#list/set/dict 자료형과 반복문, 조건부표현식 결합
# for 메모리 사용량 감소, 속도 향상
#-----
# a리스트의 데이터를 b리스트에 담기(a리스트에서 짝수*3, 홀수 그대로 b에 담기)
a=[1,2,3,4,5,6]
b=[]
for num in a:
    if num%2: b.append(num)
    else: b.append(num*3)
print(f'a=>{a}\nb=>{b}')
# 1. a리스트의 모든 원소를 새로운 리스트에 담기

#c=[]
#for num in a: c.append(num)

c=[num for num in a]

# 2. 짝수 데이터만 새로운 리스트 c에 담기

#c=[]
#for num in a:
#   if not num%2: c.append(num*3)

c=[num*3 for num in a if not num%2]

# 3. 짝수 데이터는 *3, 홀수 데이터는 그대로 새로운 리스트 c에 담기
# c=[]
# for num in a:
#     if num%2: c.append(num)
#     else: c.append(num*3)

c=[num*3 if not num%2 else num for num in a]

print(f'a=>{a}\nb=>{b}\nc=>{c}')
