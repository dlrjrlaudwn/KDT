#문자열을 구성하는 문자를 검사해주는 메서드: isXXXX() => T/F

# 알파벳으로 구성된 문자열인지 검사: isalphabet()
data='good'
print(f'{data} => {data.isalpha()}')

# 알파벳 대문자로 구성된 문자열인지 검사: isupper()
data='good'
print(f'{data} => {data.isupper()}')

print(f'GOOD => {'GOOD'.isupper()}')

# 알파벳 소문자로 구성된 문자열인지 검사: islower()
print(f'GOOD => {'GOOD'.islower()}')
print(f'Good => {'Good'.islower()}')
print(f'good => {'good'.islower()}')

# 숫자로 구성된 문자열인지 검사: isdecimal()
print(f'1234 => {'1234'.isdecimal()}')
print(f'happy1234 => {'happy1234'.isdecimal()}')

# 숫자와 문자가 혼합된 경우: isalnum()
print(f'1234 => {'1234'.isalnum()}')
print(f'happy1234 => {'happy1234'.isalnum()}')

# 공백 문자 여부 검사: isspace()
print(f'1234    => {'1234   '.isspace()}')
print(f'       => {'      '.isspace()}')

# 문자열 내에 숫자 존재여부 체크 메서드들 3종류
# - 변수명.isnumeric()  : 0~9까지의 숫자, 5¹, 5₁, ①, ➊, ⅒, Ⅳ, ⅳ, 百
# - 변수명.isdigit()    : 0~9까지의 숫자, 5¹, 5₁, ①, ➊ 
# - 변수명.isdecimal()  : 0~9까지의 숫자
#    ==> 실수, 음수, 나머지 : False
# - 확인 가능 범위:isdecimal() < isdigit() < isnumeric()
