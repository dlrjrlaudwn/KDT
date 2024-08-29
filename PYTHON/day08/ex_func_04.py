#-----
#사용자 정의 함수
#-----
#매개변수에 전달되는 데이터가 지정되지 않는 경우
# 데이터 종류:값(데이터) => 키워드 파라미터(키워드 매개변수)
# def 함수명(**params): **: '키=값' 형태 의미

#기능: 회원가입
#이름:register
#매개변수: 다 다름(가입하는 사람마다 입력하는 정보 다 다름)
#결과: 가입 메시지(str)
def register(**params):
    print(type(params))

register(name='홍길동',job='의적')
register(id='master',age=10,gender='F')
register()

#기능: 회원가입
#이름:register
#매개변수: 필수 입력 사항_id.pw.email / 선택 입력 사항_**params
#결과: 가입 메시지(str)
def register2(id,pw,email,**params):
    print(type(params))

register2('hong','h1234','h@naver.com','홍길동',job='의적')
register2('hong','h1234')
