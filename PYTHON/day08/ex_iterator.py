#-----
#iterator 객체: iterable(반복 가능한/반복자를 가지고 있는) 객체
#-----
#내장함수 dir(): 객체가 가지는 변수와 메서드를 리스트로 알려줌
nums=[11,33,55]

#_ <- 변수명으로 사용 시, 특별한 의미 없이 문법상 필요한 경우 사용 가능
for _ in dir(nums): print(_)

#리스트에서 반복자(iterator) 추출:__iter__()   <- 메서드
iterator=nums.__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())


#내장함수 iter(반복 가능한 객체): 객체에 존재하는 반복자 추출
iterator=iter(nums)
print(iterator.__next__())