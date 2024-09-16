city={'Seoul':['South Korea','Asia',9655000],
 'Tokyo':['Japan','Asia',14110000],
 'Beijing':['China','Asia',21540000],
 'London':['United Kingdom','Europe',14800000],
 'Berlin':['Germany','Europe',3426000],
 'Mexico City':['Mexico','America',21200000]}

def main():
  print()
  print('-----------------------------------------')
  print('1. 전체 데이터 출력')
  print('2. 수도 이름 오름차순 출력')
  print('3. 모든 도시의 인구수 내림차순 출력')
  print('4. 특정 도시의 정보 출력')
  print('5. 대륙별 인구수 계산 및 출력')
  print('6. 프로그램 종료')
  print('-----------------------------------------')

while True:
  main()
  main_input=int(input('메뉴를 입력하세요: '))

  if main_input==1:
    for index, (key, value) in enumerate(city.items()):
      print(f'[{index+1}] {key}:{value}')

  elif main_input==2:
    city_list = sorted(city.items())
    for index, (key, value) in enumerate(city_list):
      print(f'[{index+1}] {key.ljust(11)} : {value[0].ljust(14)} {value[1].ljust(7)} {value[2]:>10,}')

  elif main_input==3:
    city_list = sorted(city.items(), key=lambda x: x[1][2], reverse=True)
    for index, (key, value) in enumerate(city_list):
      print(f'[{index+1}] {key.ljust(11)} : {value[2]:>10,}')

  elif main_input==4:
    city_name=input('출력할 도시 이름을 입력하세요: ')
    if city_name in city:
      print(f'도시: {city_name}')
      print(f'국가: {city[city_name][0]}, 대륙: {city[city_name][1]}, 인구수: {city[city_name][2]:,}')
    else:
      print(f'{city_name}은 key에 없습니다.')
  elif main_input==5:
    continent_name=input('대륙 이름을 입력하세요(Asia, Europe, America): ')
    if continent_name in ['Asia', 'Europe', 'America']:
      continent_population = []
      for key, value in city.items():
        if value[1] == continent_name:
          continent_population.append(value[2])
          print(f'{key}:{value[2]:,}')
      print(f'{continent_name} 전체 인구수: {sum(continent_population):,}')
  else:
    print('프로그램을 종료합니다.')
    break

