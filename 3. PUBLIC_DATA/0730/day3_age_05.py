import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib

def parse_disctrict_name(city):
    '''
    '행정구역' 명칭에서 숫자 부분 제거
    - 서울특별시 종로구 (1111000000)
    '''
    city_name=re.split('[()]',city)
    return city_name[0]

def draw_piechart(city_name,city_population,voting_population):
    '''
    전체 인구수 대비 투표 가능 인구 파이차트 작성
    '''
    non_voting_population=city_population-voting_population
    population=[non_voting_population, voting_population]
    color=['#ff9999','#66b3ff']
    plt.pie(population,labels=['18세 미만','투표가능인구'],autopct='%.1f%%',colors=color,startangle=90)
    plt.legend()
    plt.title(city_name+'투표 가능 인구 비율')
    plt.show()

def get_voting_population(city):
    '''
    투표 가능 인구(row[21:]) 분석
    전체 인구수: row[1]
    '''
    f=open('age.csv',encoding='euc_kr')
    data=csv.reader(f)
    header=next(data)

    city_name=''
    city_population=0
    voting_population=0
    for row in data:
        if city in row[0]:
            city_population=row[1]
            city_population=city_population.replace(',','')
            city_population=int(city_population)
            city_name=parse_disctrict_name(row[0])
            for data in row[21:]:
                data=data.replace(',','')
                voting_num=int(data)
                voting_population+=voting_num
            break
    f.close()
    print(f'{city_name} 전체 인구수: {city_population:,}명,투표 가능 인구수: {voting_population:,}명')
    draw_piechart(city_name,city_population,voting_population)

city=input('투표 가능 인구수를 확인할 도시 이름을 입력하세요: ')
get_voting_population(city)