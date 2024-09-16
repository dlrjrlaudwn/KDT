#-----
#tuple 메서드: index/count
# 수정 불가(추가, 삭제, 변경 불가)
#-----
nums=10,20,30
idx=nums.index(20)
print(idx)

if 5 in nums:
    idx=nums.index(20)
    print(idx)

print(10,nums.count(10))   
print(5,nums.count(5))   