#-----
#내장함수
#-----
#정수 관련 내장함수
# 정수->2진수: bin(정수) => 0b(2진수) str형태
print(4,bin(4),type(bin(4)))
# 정수->8진수: oct(정수) => 0o(8진수)
print(4,oct(4),type(oct(4)))
print(8,oct(8),type(oct(8)))
# 정수->16진수: hex(정수) => 0x(16진수) 
print(4,hex(4),type(hex(4)))
print(8,hex(8),type(hex(8)))
print(17,hex(17),type(hex(17)))

#2진수->10진수: int('',base=0)
print(int('0b10',base=0))