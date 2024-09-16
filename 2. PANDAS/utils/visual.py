#-----
#시각화 관련 함수
#-----

#기능: 버전 체크 후 출력
#이름: check_version
#매개변수: None
#결과: None

def chech_version():
    import matplotlib
    print(f'matplotlib: v.{matplotlib.__version__}')