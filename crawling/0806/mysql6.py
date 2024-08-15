import pymysql

conn=pymysql.connect(host='localhost', user='root',password='1234',db='sqlclass_db',charset='utf8')
cur=conn.cursor()

sql='''
update customer
set region='서울특별시'
where region='서울'
'''

cur.execute(sql)
print('update 완료')

sql='delete from customer where name=%s'
cur.execute(sql,'홍길동')
print('delete 홍길동')

conn.commit()
cur.close()
conn.close()