#클래스(class)

#클래스 정의: 햄버거
#클래스 이름: burger
#클래스 속성: 번, 패티, 야채, 치즈
#클래스 기능: 설명

class burger:
    #__init__: 힙 영역에 객체 생성 시 속성값 저장해줌
    def __init__(self,bread,patty,veg,kind):
        self.bread=bread
        self.patty=patty
        self.veg=veg
        self.kind=kind

    #클래스의 기능(메서드)
    def printInfo(self):
        print(f'빵 종류:{self.bread}')
        print(f'패티 종류:{self.patty}')
        print(f'야채 종류:{self.veg}')
        print(f'브랜드 종류:{self.kind}')

    #속성 변경, 읽어오는 메서드: getter/setter()
    def get_bread(self):
        return self.bread
    
    def set_bread(self,bread):
        self.bread=bread



#객체 생성
burger1=burger('브리오슈','불고기','양상추 양파','롯데리아')
burger2=burger('참깨빵','소고기','치즈 양상추 양파','맥도날드')

#정보 확인
burger1.printInfo()
burger2.printInfo()

#속성 읽기: 직접 접근/간접 접근(getter 메서드 사용)
print(burger1.bread,burger1.get_bread())

#속성 변경: 직접 접근/간접 접근(setter 메서드 사용)
burger1.bread='들깨빵'
burger1.set_bread('올리브빵')