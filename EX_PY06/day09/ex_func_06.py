#-----
#람다: 한줄 함수, 익명 함수
# 형식: lambda (매개변수) : 실행 코드
#-----
names={1:'kim',2:'adam',3:'zoo'}

#key 기준으로 정렬: sorted -> list 반환
result=sorted(names)
print('오름차순 정렬', result)

#value 기준으로 정렬: sorted -> list 반환
result=sorted(names.items(),key=lambda items:items[1])
print('오름차순 정렬', result)

result=sorted('THis is a test string from Andrew'.split())
print(result)

result=sorted('THis is a test string from Andrew'.split(),key=str.lower)
print(result)

#map(), lambda
data=[11,22,33,44]
#각 원소의 값에 *2 -> 다시 리스트로 저장
def multi2(value): return value*2
data2=list(map(multi2,data))
print(data2)

data2=list(map(lambda a:a*2,data))
print(data2)