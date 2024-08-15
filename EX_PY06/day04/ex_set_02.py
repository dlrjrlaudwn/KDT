#-----
#set 연산자
#------
d1={1,3,5,7}
d2={2,4,6,8}

#덧셈 연산
# print(d1+d2)
# => 메서드 사용해야 함

#합집합
print(d1.union(d2), d1|d2)

#교집합
print(d1.intersection(d2), d1&d2)

#차집합
print(d1.difference(d2), d1-d2)
print(d2.difference(d1), d2-d1)
