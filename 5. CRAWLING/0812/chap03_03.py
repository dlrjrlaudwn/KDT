from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages=set()
count=0

def getlinks(pageurl):
    global pages
    global count

    html=urlopen('https://en.wikipedia.org{}'.format(pageurl))
    bs=BeautifulSoup(html,'html.parser')

    try:
        print(bs.h1.get_text())
        print(bs.find('div',attrs={'id':'mw-content-text'}).find('p').text)
    except AttributeError as e:
        print('this page is missing something! continuing: ',e)
        pattern='^(/wiki/)((?!:).)*$'
        for link in bs.find_all('a',href=re.compile(pattern)):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    newpage=link.attrs['href']
                    print('-'*40)
                    count+=1
                    print(f'[{count}]: {newpage}')
                    pages.add(newpage)
                    getlinks(newpage)

getlinks('')