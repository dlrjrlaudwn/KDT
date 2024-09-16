import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs=BeautifulSoup(html,'html.parser')
table=bs.find_all('table',{'class':'wikitable'})[0]
rows=table.find_all('tr')

csvfile=open('editors.csv','wt',encoding='utf-8')
writer=csv.writer(csvfile)

try:
    for row in rows:
        csvrow=[]
        for cell in row.find_all(['th','td']):
            print(cell.text.strip())
            csvrow.append(cell.text.strip())
        writer.writerow(csvrow)

finally:
    csvfile.close()