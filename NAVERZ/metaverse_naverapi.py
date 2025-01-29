import urllib.request
import json
import pandas as pd
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def get_request_url(url):
    client_id = 'FnMqvXyiWuH8vjr8riJT'
    client_secret = 'lbKzgUykJ9'
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id",client_id)
    req.add_header("X-Naver-Client-Secret",client_secret)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode()==200:
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print(f'Error for URL: {url}')

def get_naver_search(node,search_text,start,display):
    base='https://openapi.naver.com/v1/search'
    node=f'/{node}.json'
    query_string=f'{urllib.parse.quote(search_text)}'

    parameters=('?query={}&start={}&display={}'.
                format(query_string,start,display))
    
    url=base+node+parameters
    response=get_request_url(url)

    if response is None:
        return None
    else:
        return json.loads(response)

def get_post_data_news(post,json_result_list,cnt):
    title=post['title']
    description=post['description']
    org_link=post['originallink']
    link=post['link']

    json_result_list.append([title,description,org_link,link])

def main():
#뉴스 데이터 프레임 -> csv
    node='news'
    search_text='메타버스'
    cnt=0
    json_result_list_news=[]

    json_response=get_naver_search(node,search_text,1,100)
    while cnt<500:
        if (json_response is None) and (json_response['display']==0):
            break
        for post in json_response['items']:
            cnt+=1
            get_post_data_news(post,json_result_list_news,cnt)

        start=json_response['start']+json_response['display']
        json_response=get_naver_search(node,search_text,start,100)
    
    result_df_news=pd.DataFrame(json_result_list_news)
    result_df_news.to_csv('metaverse.csv',index=False,encoding='utf-8')

if __name__=='__main__':
    main()

#워드 클라우드
total=open('metaverse.csv', encoding='utf-8').read()
okt=Okt()

sentences_tag=[]
sentences_tag=okt.pos(total)

noun_adj_list=[]

for word,tag in sentences_tag:
    if tag in ['Noun','Adjective','Alpha']:
        noun_adj_list.append(word)

counts=Counter(noun_adj_list)
tags=counts.most_common(100)

tag_dict=dict(tags)
stopwords=['메타','버스','등','사업','플랫폼','기술','기업','의','및','이번','이','있다','과','발표','생','수','것','위','은',
           '글로벌','수출','한국','증가','팀','대한','있는','통해','를','있습니다', '전망',' 관련','취업', '로', '별','올해',
           '주요','최근','quot','b','관련','개월','토피아','파악','업계', '산업', '기반']

for stopword in stopwords:
    if stopword in tag_dict:
        tag_dict.pop(stopword)

path=r'c:\Windows\Fonts\malgun.ttf'


wc=WordCloud(font_path=path,width=400,height=400,
                background_color='#EBEBEA',max_font_size=150,
                repeat=True,colormap='tab20')

cloud=wc.generate_from_frequencies(tag_dict)

plt.figure(figsize=(10,8))
plt.axis('off')
plt.imshow(cloud)
plt.show()