import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f=open('gender.csv',encoding='euc-kr')
data=csv.reader(f)
city_list=['대구광역시','대구광역시 중구','대구광역시 동구','대구광역시 서구','대구광역시 남구','대구광역시 북구','대구광역시 수성구','대구광역시 달서구','대구광역시 달성군','대구광역시 군위군']

fig=plt.figure(figsize=(10,10))
axes=fig.subplots(5,2)

index = 0

for city in city_list:
  male_list=[]
  female_list=[]
  population = []

  for row in data:
    if city in row[0]:
      for i in range(106,207):
        male_list.append(int(row[i].replace(',','')))
        female_list.append(int(row[i+103].replace(',','')))
      break

  print(f'{city} : (남:{sum(male_list):,} 여:{sum(female_list):,})')

  population.append([sum(male_list), sum(female_list)])

  i = index // 2
  j = index % 2

  axes[i,j].pie(population[0], labels=['남성', '여성'],autopct='%.1f%%',startangle=90) # Use population[0] as it's the only element
  axes[i,j].set_title(city)

  index += 1

plt.tight_layout()
plt.suptitle('대구광역시 구별 남녀 인구 비율')
plt.show()