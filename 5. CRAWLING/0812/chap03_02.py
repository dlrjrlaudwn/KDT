from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re

random.seed(None)

def getlinks(articleurl):
    html=urlopen('https://en.wikipedia.org'+articleurl)
    bs=BeautifulSoup(html,'html.parser')
    bodyContent=bs.find('div',{'id':'bodyContent'})
    wikiurl=bodyContent.find_all('a',href=re.compile('^(/wiki/)((?!:).)*$'))
    return wikiurl

links=getlinks('/wiki/Kevin_Bacon')
print('links 길이: ',len(links))
while len(links)>0:
    newarticle=links[random.randint(0,len(links)-1)].attrs['href']
    print(newarticle)
    links=getlinks(newarticle)