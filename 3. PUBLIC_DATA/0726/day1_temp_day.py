import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def draw_graph_on_date(month,day):
    f=open('daegu-utf8.csv', encoding='utf-8-sig')
    data=csv.reader(f)
    next(data)
    result=[]
    for row in data:
        if row[-1]!='':
            date_string=row[0].split('-')
            if date_string[1]==month and date_string[2]==day:
                result.append(float(row[-1]))

    f.close()
    plt.figure(figsize=(15,2))
    plt.plot(result,color='royalblue')
    plt.rc('axes',unicode_minus=False)
    plt.title(f'{month}월 {day}일 대구 최고 기온')
    plt.show()


month,date=input('날짜를 입력하세요(월/일):').split()
draw_graph_on_date(month,date)