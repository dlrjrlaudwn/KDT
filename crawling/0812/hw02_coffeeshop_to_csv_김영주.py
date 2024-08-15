from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
from tabulate import tabulate as tbl

location_list=[]
name_list=[]
address_list=[]
num_list=[]

for i in range(1,50):
    html=urlopen(f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store=')
    soup=BeautifulSoup(html,'html.parser')
    hollys=soup.find_all('td')

    for j in range(10):
        location=hollys[6*j].text
        name=hollys[6*j+1].text
        address=hollys[6*j+3].text
        num=hollys[6*j+5].text

        location_list.append(location)
        name_list.append(name)
        address_list.append(address)
        num_list.append(num)

html=urlopen(f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=50&sido=&gugun=&store=')
soup=BeautifulSoup(html,'html.parser')
hollys=soup.find_all('td')

for j in range(5):
    location=hollys[6*j].text
    name=hollys[6*j+1].text
    address=hollys[6*j+3].text
    num=hollys[6*j+5].text

    location_list.append(location)
    name_list.append(name)
    address_list.append(address)
    num_list.append(num)

df=pd.DataFrame({'지역':location_list,'매장 이름':name_list,'주소':address_list,'전화번호':num_list})
print(tbl(df,headers='keys',tablefmt='psql'))

df.to_csv('hollys_branches.csv', index=False,encoding='utf-8')

for n in range(len(df)):
    print(f"[{n+1:3}]: 매장이름: {df.loc[n,'매장 이름']}, 지역: {df.loc[n,'지역']}, 주소: {df.loc[n,'주소'],}, 전화번호: {df.loc[n,'전화번호']}")