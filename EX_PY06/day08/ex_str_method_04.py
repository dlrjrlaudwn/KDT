#문자열에서 원소/요소 변경해주는 메서드: replace()

msg='Pithon'

msg[1]='Y'  #인덱스로 요소 변경 불가(미지원 기능) => 전용 메서드 활용해야 함

m1=msg.replace('i','y')  #복사본 형태로 출력 => 저장 필요
print(f'msg:{msg} --- m1:{m1}')

msg=msg.replace('i','y')  
print(f'msg:{msg} --- m1:{m1}')

msg='good happy'
# 'o'를 'O'로 변경
print(msg.replace('o','O'))

# 'o'를 'O'로 1개만 변경
print(msg.replace('o','O',1))