#--------------
#내장함수 print() 사용법
# print함수의 매개변수
# 매개변수(parameter): 함수 코드 실행 시 필요한 데이터를 명시해놓은 것
#  file 매개변수: 데이터를 파일에 기록
#--------------
#파일 읽기/쓰기
# 파일 열기 open()
# 파일 읽기/쓰기
# 파일 닫기 close()
FILENAME='result.txt'

#파일을 쓰기모드(w)로 열기
f=open(FILENAME, mode='w')
#f.write('Hello')
#파일에 데이터 출력
print("good luck", file=f)
#파일 닫기
f.closes