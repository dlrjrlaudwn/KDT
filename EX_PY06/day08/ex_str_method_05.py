#1개의 문자열을 여러개의 문자열로 분리: split()
# 기본값: 공백을 기준으로 분리

msg=' happy new year '
result=msg.split()
print(f'result: {type(result)},{result}')

phone='010-1111-2222'
presult=phone.split('-')
print(f'presult: {type(presult)},{presult}')

msg='오늘은 날씨가 좋군요. 내일도 날씨가 좋을까요?'
result=msg.split('.')
print(f'result: {type(result)},{result}')

#여러개의 문자열을 1개의 문자열로 합치기: join()
# 합칠문자.join(여러 개 문자열)

# 010*1111*2222
phone2='*'.join(presult)
print(phone2)
#010_1111_2222
con='_'
phone2=con.join(presult)
print(phone2)
