#-----
#반복문: 유사하거나 동일한 코드를 1번 작성해서 재사용하기 위한 방법
# 종류: for, while
#-----
# for 반복문: 시퀀스(이터러블) 데이터에서 원소/요소 하나씩 읽어올 때 사용
# for (변수명) in (시퀀스/이터러블 데이터):
#   반복할 코드
#-----
#문자열에서 문자를 1줄에 1개씩 출력
msg='merry christmas 2025'
for m in msg:
    print(m) #뒤에 end=' ' 붙이면 옆으로 씀
print('END')

#코드값 같이 출력
for m in msg:
    print(m,ord(m))
print('END')
#-----
#리스트에서 원소 하나씩 읽어오기
# 1~100 범위에서 3의 배수만 저장한 리스트
data=list(range(3,101,3))
for d in data:
    print(d,end=' ')
print('END')

#str 타입의 원소를 가지는 리스트: 해당 원소를 정수로 형변환시켜 저장하기
# 원래 원소의 값을 변경하려면 인덱스 필요: 원소의 개수로 인덱스 범위 파악
data=['4','9','1','3','8']
print('전',data)
for d in data:
    int(d)

#리스트의 인덱스 가져오기
for idx in range(len(data)):
    print(f'idx=>{idx}')
    data[idx]=int(data[idx])

print('후',data)