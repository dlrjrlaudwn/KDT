class vendigmachine:
    def __init__(self,input_dict):
        '''
        생성자
        :param input_dict: 초기 자판기 재료량(dict 형태)
        '''
        self.input_money=0
        self.inventory=input_dict

    def run(self):
        '''
        커피 자판기 동작 및 메뉴 함수 호출
        '''
        self.input_money=int(input('동전을 투입하세요: '))

        while True: 
            #300원보다 적게 넣으면 반환
            if self.input_money<300:
                print(f'투입된 돈({self.input_money}원)이 300원보다 작습니다.')
                print(f'{self.input_money}원을 반환합니다.')
                break

            else:
                print('-'*100)
                print(f'  커피 자판기 (잔액: {self.input_money-self.inventory["change"]}원)')
                print('-'*100)
                print('1. 블랙 커피')
                print('2. 프림 커피')
                print('3. 설탕 프림 커피')
                print('4. 재료 현황')
                print('5. 종료')
                print()
                menu=int(input('메뉴를 선택하세요: '))
                print()

            #블랙커피: 커피 30, 물 100, 컵 1
            #크림커피: 커피 15, 크림 15, 물 100, 컵 1
            #설탕크림커피: 커피 10, 크림 10, 설탕 10, 물 100, 컵 1

            if (self.inventory['coffee']<10) or (self.inventory['cream']<10) or (self.inventory['sugar']<10) or (self.inventory['water']<100) or (self.inventory['cup']==0):
                print('재료가 부족합니다.')
                print('-'*100)
                print('재료 현황: ', end='')
                for k, v in self.inventory.items():
                    print(f'{k}: {v}', end='  ')
                print()
                print('-'*100)
                print(f'{self.input_money-self.inventory["change"]}원을 반환합니다.')
                self.inventory['change']=0
                break

            if menu == 5:
                print(f'종료를 선택하셨습니다. {self.input_money-self.inventory["change"]}원이 반환됩니다.')
                break

            elif menu==2:
                while True:
                    if self.input_money>=300:
                        if self.inventory['coffee']>=15 and self.inventory['cream']>=15 and self.inventory['water']>=100 and self.inventory['cup']>=1:
                            self.inventory['coffee']-=15
                            self.inventory['cream']-=15
                            self.inventory['water']-=100
                            self.inventory['cup']-=1
                            self.inventory['change']+=300
                            print(f'프림 커피를 선택하셨습니다. 잔액: {self.input_money-self.inventory["change"]}')

                            break

            elif menu==1:
                while True:
                    if self.input_money>=300:
                        if self.inventory['coffee']>=30 and self.inventory['water']>=100 and self.inventory['cup']>=1:
                            self.inventory['coffee']-=30
                            self.inventory['water']-=100
                            self.inventory['cup']-=1
                            self.inventory['change']+=300
                            print(f'블랙 커피를 선택하셨습니다. 잔액: {self.input_money-self.inventory["change"]}')
                            break            

            elif menu==3:
                while True:
                    if self.input_money>=300:
                        if self.inventory['coffee']>=10 and self.inventory['cream']>=10 and self.inventory['sugar']>=10 and self.inventory['water']>=100 and self.inventory['cup']>=1:
                            self.inventory['coffee']-=10
                            self.inventory['cream']-=10
                            self.inventory['sugar']-=10
                            self.inventory['water']-=100
                            self.inventory['cup']-=1
                            self.inventory['change']+=300
                            print(f'설탕 프림 커피를 선택하셨습니다. 잔액: {self.input_money-self.inventory["change"]}')
                            break     

            print('-'*100)
            print('재료 현황: ', end='')
            for k, v in self.inventory.items():
                print(f'{k}: {v}', end='  ')
            print()
            print('-'*100)

            if self.input_money-self.inventory["change"]<300:
                print(f'잔액({self.input_money-self.inventory["change"]}원)이 300원보다 작습니다. ')
                print(f'{self.input_money-self.inventory["change"]}원을 반환합니다.')
                break



        print('-'*100)
        print('커피 자판기 동작을 종료합니다.')
        print('-'*100)

inventory_dict={'coffee':100, 'cream':100, 'sugar':100,'water':500, 'cup':5, 'change':0}
coffee_machine=vendigmachine(inventory_dict)
coffee_machine.run()