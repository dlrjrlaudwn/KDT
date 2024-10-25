import pymysql
import requests
from PIL import Image
from io import BytesIO
import os
import time

connect = pymysql.connect(host='155.230.153.151', user='songeun', password='1234', db='songeun', charset='utf8mb4')
cur = connect.cursor()

query = 'select * from fashiondf'
cur.execute(query)
connect.commit()

acc=['Watches', 'Socks', 'Belts', 'Bags', 'Shoe Accessories', 'Jewellery', 'Eyewear',
       'Scarves', 'Wallets', 'Headwear', 'Mufflers', 'Ties', 'Accessories', 'Gloves',
       'Sports Accessories', 'Cufflinks', 'Stoles', 'Umbrellas', 'Wristbands']

datas = cur.fetchall()
for index, data in enumerate(datas):
    for attempt in range(3):  
        try:
            response = requests.get(data[0], timeout=10)  
            response.raise_for_status()  

            img = Image.open(BytesIO(response.content))

            if data[1] in acc:
                filename = rf'C:\Users\MSI\Desktop\KDT\FLASK_AI\1024\data\1\image_{index}.jpg'
                print(data[0], data[1])
            else:
                filename = rf'C:\Users\MSI\Desktop\KDT\FLASK_AI\1024\data\0\image_{index}.jpg'

            img.save(filename)
            break  

        except (requests.exceptions.RequestException, OSError) as e:
            print(f"Attempt {attempt + 1} failed for {data[0]}: {e}")
            time.sleep(1)  

cur.close()
connect.close()
