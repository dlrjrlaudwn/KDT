#------
#문자 1개의 코드값을 저장하는 조건식 작성(알파벳은 코드값으로 변환, 그 외에는 None으로 코드값 전달)
#------
data='m'
result=None
if ('a'<=data<='Z'or'A'<=data<='Z'):
    result=ord(data)
else:
    result=None
print(f'{data}의 코드값: {result}')
# 조건부 표현식
result=ord(data) if ('a'<=data<='Z'or'A'<=data<='Z') else None
print(f'{data}의 코드값: {result}')