#001
print('Hello World')

#002
print("Mary's cosmetics")

#003
print('신씨가 소리질렀다. "도둑이야".')

#004
print('C:\Windows')

#005
print("안녕하세요.\n만나서\t\t반갑습니다.")
#\n: 줄바꿈, \t: 탭간격

#006
print ("오늘은", "일요일")
# 오늘은 일요일

#007
print('naver','kakao','sk','samsung', sep=';')

#008
print('naver','kakao','sk','samsung', sep='/')

#009
print("first",end='');print("second")

#010
print(5/3)

#011
삼성전자=50000
총평가금액=삼성전자*10
print(총평가금액)

#012
시가총액='298조'
현재가=50000
per=15.79
print(시가총액)
print(현재가)
print(per)

#013
s = "hello"
t = "python"
print(s+'!', t)

#014
print(2+2*3)

#015
a='132'
print(type(a))

#016
num_str=720
int=int(num_str)
print(int, type(int))

#017
num=100
str=str(num)
print(str, type(str))

#018
a='15.79'
a=float(a)
print(a, type(a))

#019
year = "2020"
del int
print(int(year)-3)  
print(int(year)-2)  
print(int(year)-1)  

#020
print(48584*36)

#021
letters='python'
print(letters[0], letters[2])

#022
license_plate = "24가 2210"
print(license_plate[-4:])

#023
string = "홀짝홀짝홀짝"
print(string[::2])

#024
string = "PYTHON"
print(string[::-1])

#025
phone_number = "010-1111-2222"
print(phone_number.replace('-', ' '))

#026
phone_number = "010-1111-2222"
print(phone_number.replace('-', ''))

#027
url = "http://sharebook.kr"
print(url.split('.')[-1])

#028
#lang = 'python'
#lang[0] = 'P'
#print(lang)

#029
string = 'abcdfe2a354a32a'
print(string.replace('a','A'))

#030
string = 'abcd'
string.replace('b', 'B')
print(string)

#031
a = "3"
b = "4"
print(a + b)

#032
print("Hi" * 3)

#033
print("-" * 80)

#034
t1 = 'python'
t2 = 'java'
print((t1+' '+t2+' ')*4)

#035
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f'이름: %s 나이: %d' %(name1, age1))
print(f'이름: %s 나이: %d' %(name2, age2))

#036
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print('이름: {} 나이: {}'. format(name1, age1))
print('이름: {} 나이: {}'. format(name2, age2))

#037
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

#038
상장주식수 = "5,969,782,550"
a=상장주식수.replace(',','')
print(int(a), type(int(a)))

#039
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

#054
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)

#055
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

#056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs=lang1+lang2
print(langs)

#057
nums = [1, 2, 3, 4, 5, 6, 7]
print('max: ', max(nums))
print('min: ', min(nums))

#058
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

#060
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))

#061
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#063
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

#064
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

#070
data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data))

#071
my_variable=()

#072
movie_rank=('닥터 스트레인지','스플릿','럭키')

#073
tuple=(1,)

#074
t = (1, 2, 3)
t[0] = 'a'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t[0] = 'a'
TypeError: 'tuple' object does not support item assignment
#tuple은 수정 불가

#075
t = 1, 2, 3, 4
print(type(t))

#076
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')

#077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data=list(interest)

#078
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data=tuple(interest)

#079
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
#apple banana cake

#080
data=tuple(range(2,99,2))