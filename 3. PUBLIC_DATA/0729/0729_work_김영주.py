"""
지하철 각 노선별 최대 하차 인원을 막대그래프로 표시하고, 하차인원 출력
- 출근 시간대: 07:00~08:59
- 사용 파일: subwaytime.csv	또는 subway.xls
  - 07:00~07:59 하차: index[11]
  -	08:00~08:59 하차: index	[13]
- 각 지하철 노선별 가장 많이 내리는 지하철 역 분석
  - 1 호선, 2 호선, 3 호선, 4 호선, 5 호선, 6 호선, 7 호선
- 하차 인원은 1,000 단위로 콤마를 찍어서 구분할 것
- 7 개의 지하철 역을 막대 그래프로 표시
- Bar	chart 의 x 축은 (노선 +	지하철 역 이름)을 표시하고, y 축은 인원수를 표시
"""

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

max_passengers = {line: (0, '') for line in ['1호선', '2호선', '3호선', '4호선', '5호선', '6호선', '7호선']}

with open('subwaytime.csv', encoding='utf-8') as f:
    data = csv.reader(f)
    next(data)
    next(data)

    for row in data:
        row[4:] = map(int, row[4:])
        total_passenger = sum(row[11:14:2])
        line = row[1]
        if line in max_passengers and total_passenger > max_passengers[line][0]:
            max_passengers[line] = (total_passenger, row[3])

for line, (passengers, station) in max_passengers.items():
    if passengers > 0:
        print(f'출근 시간대 {line} 최대 하차역: {station}역, 하차인원: {passengers:,}명')


plt.figure(figsize=(10, 6))
plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역')
plt.bar([station for station, _ in max_passengers.items()], [passengers for passengers, _ in max_passengers.values()])
plt.xticks(rotation=70)
plt.show()

