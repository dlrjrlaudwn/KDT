#-----
#문자열을 기계어(2진수)로 변환해서 저장
# ex) 입력: Hello => 출력: (2진수)
#-----
msg='ABC'
result=''
for m in msg:
    result=result+bin(ord(m))[2:]
    print(result)
#-----
#원소/요소의 인덱스와 값을 함께 가져오기
#-----
nums=[11,33,55]
#원소/요소 데이터만 가져오기
for n in nums:
    print(n)

#원소에 인덱싱 부여한 객체 변환: enumerate()
print('enumerate() 변환:',list(enumerate(nums)))

#원소/요소&인덱스 가져오기: enumerate()
# enumerate(): 전달된 반복가능한 객체에서 원소당 번호 부여 -> 튜플로 묶어줌
#            : 원소의 인덱스 정보가 필요한 경우 사용   
for idx,n in enumerate(nums):
    print(idx,n)
for e in enumerate(nums):
    print(e)

nums=['11','33','55']
for e in enumerate(nums):
    nums[e[0]]=int(e[1])
    
for idx,data in enumerate(nums):
    nums[idx]=int(data)