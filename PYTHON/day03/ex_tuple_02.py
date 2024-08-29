#-----
#내장함수(len(), max(), min(), sum()), 연산자(덧셈, 곱셈, 멤버)
#-----
nums=11,22,33,44,55

#내장함수
print(f'nums 개수: {len(nums)}개')
print(f'최댓값: {max(nums)} 최솟값: {min(nums)}')
print(f'합계: {sum(nums)}')
print(f'정렬: {sorted(nums)}')
print(f'정렬: {sorted(nums)}, {sorted(nums, reverse=True)}')

print(max('abc', 'abC'))
print(sorted(['abc', 'Zoo']))
# print(sum(['abc','Zoo']))

#연산자
data1=11,22
data2='A','B','C'
data3=[1,2]

print(data1+data2)
# print(data1+data3)
print(data1+tuple(data3))

# print(data1*data2)
print(data1*3)

print(11 in data1)
print('A' in data1)