#사용자가 'q/Q' 입력하기 전까지 계속 데이터 입력받고, 'q/Q'를 입력하면 중단

while True:
    data=input()
    if data=='q' or data=='Q': break

print('END')