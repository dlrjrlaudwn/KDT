from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    page=urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
    html=BeautifulSoup(page.read(), 'html.parser')

    scraping_use_find(html)
    print()
    scraping_use_select(html)


def scraping_use_find(html):
    total_find=html.find_all('div',{'class':'tombstone-container'})
    print('[find 함수 사용]')
    print(f'총 tombstone-container 검색 개수: ', len(total_find))

    for day in total_find: 
        p_name=day.find('p',{'class':'period-name'})
        s_desc=day.find('p',{'class':'short-desc'})
        img=day.find('img',{'class':'forecast-icon'})
        low_temp=day.find('p',{'class':'temp'})
        if low_temp is not None:
            temp=low_temp.text
        else:
            temp=''

        print('-'*100)
        print('[Period]: ',p_name.text)
        print('[Short desc]: ', s_desc.text)
        print('[Temperature]: {0}'.format(temp))
        print('[Image desc]: ',img.attrs['title'])


def scraping_use_select(html):
    total_select=html.select('.tombstone-container')
    print('[select 함수 사용]')
    print(f'총 tombstone-container 검색 개수: ', len(total_select))

    for day in total_select: 
        p_name=day.select_one('.period-name')
        s_desc=day.select_one('.short-desc')
        img=day.select_one('.forecast-icon')
        low_temp=day.select_one('.temp')
        if low_temp is not None:
            temp=low_temp.text
        else:
            temp=''

        print('-'*100)
        print('[Period]: ',p_name.text)
        print('[Short desc]: ', s_desc.text)
        print('[Temperature]: {0}'.format(temp))
        print('[Image desc]: ',img.attrs['title'])

main()