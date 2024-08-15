from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def gettitle(url,tag):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    
    try:
        bsobj=BeautifulSoup(html.read(),'html.parser')
        value=bsobj.body.find(tag)
    except AttributeError as e:
        return None
    return value

tag='h2'
value=gettitle('http://www.pythonscraping.com/pages/page1.html', tag)

if value==None:
    print(f'{tag} could not be found')
else:
    print(value)