import matplotlib.pyplot as plt
import koreanize_matplotlib

plt.plot([-1,0,1,2])
plt.title('그래프 제목', fontweight='bold')
plt.xlabel('간단한 그래프')
plt.show()

import csv

f=open('daegu.csv','r',encoding='utf-8-sig')
data=csv.reader(f,delimiter=',')
count=0
for row in data:
    if count>5:
        break
    else:
        print(row)
    count+=1

f.close()

import csv
fin=open('daegu.csv','r',encoding='utf-8-sig')
data=csv.reader(fin,delimiter=',')
fout=open('daegu-utf8.csv','w',encoding='utf-8-sig')
wr=csv.writer(fout)

for row in data:
    for i in range(len(row)):
        row[i]=row[i].replace('\t','')
    print(row)
    wr.writerow(row)

fin.close()
fout.close()
print('파일 저장 완료')

