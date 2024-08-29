#-----
#문자열 원소/요소 변경
#-----
msg='pithon'

#1. 원소/요소 값 변경
msg[1]='y'

#2. 원소/요소 값 삭제: del(), del
del(msg[1])
del msg[1]

#명령어 del(), del
del(msg)  #변수 msg 삭제됨

print(msg)