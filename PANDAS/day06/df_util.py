#------
#series/dataframe에서 사용되는 사용자 정의 함수
#------

#기능: df의 기본 정보, 속성 확인
#이름: checkdf
#매개변수: df 인스턴스(변수명), df 이름
#반환값: X
def checkdf(object,name):
    print(f'\n[{name}]')
    object.info()
    print(f'[index]:{object.index}')
    print(f'[columns]:{object.columns}')
    print(f'[ndim]:{object.ndim}')