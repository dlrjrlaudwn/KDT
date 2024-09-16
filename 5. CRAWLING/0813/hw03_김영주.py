from urllib.request import urlopen
from bs4 import BeautifulSoup
import  requests
import collections
if not hasattr(collections,'Callable'):
    collections.Callable=collections.abc.Callable

html=requests.get('https://finance.naver.com/sise/sise_market_sum.naver')
soup=BeautifulSoup(html.text,'html.parser')

top10=soup.find_all('a',{'class':'tltle'})

top10_list=[]
company_url=[]
total_list=[]
code3_list=[]
now_list=[]
past_list=[]
price_list=[]
high_list=[]
low_list=[]

for i in top10[:10]:
    top10_list.append(i.text)
    if 'href' in i.attrs:
        company_url.append(i.attrs['href'])

for j in range(len(company_url)):
    base='https://finance.naver.com/'
    plus=f'{company_url[j]}'
    total=base+plus
    total_list.append(total)

for total in total_list:
    html2=urlopen(total)
    soup=BeautifulSoup(html2,'html.parser')
    code=soup.find('dl',{'class':'blind'})
    code2=code.find_all('dd')
    code3=code2[2].text.split()[1]
    now=code2[3].text.split()[1]
    past=code2[4].text.split()[1]
    price=code2[5].text.split()[1]
    high=code2[6].text.split()[1]
    low=code2[8].text.split()[1]
    code3_list.append(code3)
    now_list.append(now)
    past_list.append(past)
    price_list.append(price)
    high_list.append(high)
    low_list.append(low)

print(code3_list)

while True:
    print('-'*35)
    print('[네이버 코스피 상위 10대 기업 목록]')
    print('-'*35)
    for j in range(len(top10_list)):
        print(f'[{j+1:2}] {top10_list[j]}')

    start=int(input('주가를 검색할 기업의 번호를 입력하세요(-1: 종료): '))

    if start==-1:
        print('프로그램 종료')
        break
    else:
        print(total_list[start-1])
        print(f'종목명: {top10_list[start-1]}')
        print(f'종목코드: {code3_list[start-1]}')
        print(f'현재가: {now_list[start-1]}')
        print(f'전일가: {past_list[start-1]}')
        print(f'시가: {price_list[start-1]}')
        print(f'고가: {high_list[start-1]}')
        print(f'저가: {low_list[start-1]}')
