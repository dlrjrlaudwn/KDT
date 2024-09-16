import csv

def get_index_of_age_csv():
    f=open('age.csv', encoding='euc_kr')
    data=csv.reader(f)
    header=next(data)
    print('-'*20)
    print('age.csv index')
    print('-'*20)
    for i in range(len(header)):
        print(f'[{i:3}]:{header[i]}')

    f.close()

get_index_of_age_csv()