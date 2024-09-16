import pymysql
import pandas as pd
import pymysql.cursors
import matplotlib.pyplot as plt
import koreanize_matplotlib

conn=pymysql.connect(host='172.20.60.116', user='member3',password='1234',db='sql_project',charset='utf8')
cur=conn.cursor(pymysql.cursors.DictCursor)
cur.execute('select * from wage_region')

rows=cur.fetchall()

#데이터 가공

wage_df=pd.DataFrame(rows)

wage_df = wage_df.set_index('지역별')

sd=wage_df.loc[['경기','인천']].mean(numeric_only=True)
gs=wage_df.loc[['부산','대구','울산','경북','경남']].mean(numeric_only=True)
jr=wage_df .loc[['광주','전북','전남']].mean(numeric_only=True)
ch=wage_df .loc[['대전','세종','충북','충남']].mean(numeric_only=True)
se=wage_df.loc['서울'].copy()
gw=wage_df.loc['강원'].copy()
jj=wage_df.loc['제주'].copy()

sd['지역']='경기/인천'
gs['지역']='경상도'
jr['지역']='전라도'
ch['지역']='충청도'
se['지역']='서울'
gw['지역']='강원도'
jj['지역']='제주도'

region_df=pd.DataFrame([se,sd,ch,gw,gs,jr,jj])
region_df=region_df[['지역','상용근로일수 (일)','상용총근로시간 (시간)','상용소정실근로시간 (시간)','상용초과근로시간 (시간)',
                    '상용월급여액 (원)','상용정액급여 (원)','상용초과급여 (원)','상용특별급여 (원)']]
region_df.columns=['region','working_day','working_time','working_real_time','working_over_time','wage','reg_wage','over_wage','special_wage']
#print(region_df)

cur=conn.cursor()
sql='''insert into region_wage
        (region,working_day,working_time,working_real_time,working_over_time,
        wage,reg_wage,over_wage,special_wage)
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

for idx in region_df.index:
    a=region_df.loc[idx].to_list()
    cur.execute(sql,a)
    conn.commit()

#지역별 평균 임금 그래프

plt.figure()
plt.bar('region','wage',data=region_df,width=0.5)
plt.title('2023 지역별 월 평균 급여액')
plt.xlabel('지역')
plt.ylabel('임금')
plt.grid(True,linestyle='--')
plt.show()

cur.close()
conn.close()