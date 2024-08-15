import csv
csvfile=open('test.csv','w',encoding='utf-8')
try:
    writer=csv.writer(csvfile)
    writer.writerow(('number','number+2','(number+2)^2'))

    for i in range(10):
        writer.writerow((i,i+2,pow(i+2,2)))
        
except Exception as e:
    print(e)

finally: 
    csvfile.close()