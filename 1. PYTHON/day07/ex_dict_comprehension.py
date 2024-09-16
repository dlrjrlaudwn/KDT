#-----
#dict 자료형과 반복문, 조건부표현식 결합
# for 메모리 사용량 감소, 속도 향상
#-----
keys=['a','b','c','d']
x={key:value for key,value in dict.fromkeys(keys).items()}
print(x)

x={key:value for key,value in dict.fromkeys(keys).items()}
print(x)