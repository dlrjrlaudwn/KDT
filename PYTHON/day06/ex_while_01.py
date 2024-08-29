#-----
#while 반복문
#-----
num=10
while num>0:
    print(num)
    num=num-1   

#-----
#리스트 원소 읽기
nums=[11,22,33]
cnt=0
while cnt<len(nums):
    print(cnt,nums[cnt])
    cnt=cnt+1

#'hello'문자열의 원소 하나씩 출력하기
msg='hello'
idx=0
while idx<len(msg):
    print(idx,msg[idx])
    idx=idx+1