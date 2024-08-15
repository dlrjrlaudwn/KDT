import pandas as pd
from tabulate import tabulate as tbl

hdf=pd.read_csv('hollys_branches.csv')
hdf.index=hdf.index+1
# print(tbl(hdf.head(), headers='keys', tablefmt='psql'))

while True:
    start=input('검색할 매장의 지역을 입력하세요: ')
    # hdf2 = hdf[hdf['주소'].map(lambda x:all(st in x for st in start))]
    # print(hdf2)

    if start=='quit':
        print('종료 합니다.')
        break
    else: 
        if start not in hdf:
            print('검색된 매장이 없습니다.')
        else: 
            hdf2 = hdf[hdf['주소'].map(lambda x:all(st in x for st in start.split()))]
            hdf2.reset_index(inplace=True)
            hdf2.drop('index',axis=1,inplace=True)
            hdf2.index=hdf2.index+1
            print('검색된 매장 수: ',len(hdf2))
            print(tbl(hdf2,headers='keys',tablefmt='psql'))




