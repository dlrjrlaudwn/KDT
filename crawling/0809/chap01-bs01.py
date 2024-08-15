from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://www.pythonscraping.com/pages/page1.html')
bs=BeautifulSoup(html.read(),'html.parser')
print(bs)
print(bs.h1)
print(bs.h1.string)
print(bs.div)         #<div> (내용) </div>
print(bs.div.text)    #텍스트 내용만