import pandas as pd
from bs4 import BeautifulSoup
import collections
if not hasattr(collections,'Callable'):
    collections.Callable=collections.abc.Callable
from selenium import webdriver
import matplotlib.pyplot as plt
import koreanize_matplotlib
from tabulate import tabulate


sk_driver=webdriver.Chrome()
sk_driver.get('https://finance.naver.com/item/coinfo.naver?code=000660')

sk_driver.switch_to.frame('coinfo_cp')

sk_html=sk_driver.page_source
bs=BeautifulSoup(sk_html, 'html.parser')

sk_table=bs.find_all('tbody')

# cnt=0
# for i in roe:
#     cnt+=1
#     print(cnt)
#     print(i)
#     print('-'*80)

sk_row=sk_table[12]
sk_cash=sk_row.find_all('tr')
sk_cash2=sk_cash[14]
sk_roe=sk_cash[21]
sk_per=sk_cash[26]
sk_pbr=sk_cash[28]
sk_cash_flow=sk_cash2.find_all('span',{'class':'cUp'})
sk_roe2=sk_roe.find_all('span',{'class':'cBk'})
sk_roe3=sk_roe.find_all('span',{'class':'cUp'})
sk_per2=sk_per.find_all('span',{'class':'cBk'})
sk_per3=sk_per.find_all('td',{'class':'num'})
sk_pbr2=sk_pbr.find_all('span',{'class':'cBk'})

sk_c_list=[]
for c in sk_cash_flow:
    sk_c_list.append(c.text)

sk_roe_list=[]
for r in sk_roe2:
    sk_roe_list.append(r.text)
for r in sk_roe3:
    sk_roe_list.append(r.text)

sk_p_list=[]
for p in sk_per2:
    sk_p_list.append(p.text)
for p in sk_per3:
    sk_p_list.append(p.text)

sk_pbr_list=[]
for p in sk_pbr2:
    sk_pbr_list.append(p.text)

sk_c_dict={'2021':sk_c_list[0],'2022':sk_c_list[1],'2023':sk_c_list[2]}
# print(sk_c_dict)

# print(sk_roe_list)
sk_r_dict={'2021':sk_roe_list[0],'2022':sk_roe_list[1],'2023':sk_roe_list[-2]}
# print(sk_r_dict)

# print(sk_p_list)
sk_p_dict={'2021':sk_p_list[0],'2022':sk_p_list[1],'2023':0}
# print(sk_p_dict)

#per이 마이너스(기업이 손해를 본 경우)인 경우 밝히지 않으므로 0으로 처리

# print(sk_pbr_list)
sk_pbr_dict={'2021':sk_pbr_list[0],'2022':sk_pbr_list[1],'2023':sk_pbr_list[2]}
# print(sk_pbr_dict)

sk=pd.DataFrame([sk_c_dict,sk_r_dict,sk_p_dict,sk_pbr_dict],index=['투자활동현금흐름','ROE','PER','PBR'])
# print(tabulate(sk,headers='keys',tablefmt='psql'))
sk.loc['투자활동현금흐름']=sk.loc['투자활동현금흐름'].str.replace(',','')
# print(tabulate(sk,headers='keys',tablefmt='psql'))
sk['2021']=sk['2021'].astype('float')
# print(tabulate(sk,headers='keys',tablefmt='psql'))

sk['2022']=sk['2022'].astype('float')
# print(tabulate(sk,headers='keys',tablefmt='psql'))

sk['2023']=sk['2023'].astype('float')
# print(tabulate(sk,headers='keys',tablefmt='psql'))
sk=sk.T
print(tabulate(sk,headers='keys',tablefmt='psql'))

def plot_maker(x,y,title,color):
    plt.plot(x,y,'o:',color=color)
    plt.title(title)
    plt.grid(linestyle=':')
    for i in range(len(x)):
        height = y[i]
        plt.text(x[i], height + 0.25, f'{y[i]:,}', ha='left', va='bottom', size = 12)
    current_values = plt.gca().get_yticks()
    plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])
    plt.tight_layout()
    plt.show()

def plot_maker2(x,y,title,color):
    plt.plot(x,y,'o:',color=color)
    plt.title(title)
    plt.grid(linestyle=':')
    for i in range(len(x)):
        height = y[i]
        plt.text(x[i], height + 0.25, '%.0f' %height, ha='center', va='bottom', size = 12)
    current_values = plt.gca().get_yticks()
    plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])
    plt.tight_layout()
    plt.show()

def plot_maker3(x,y,title,color):
    plt.plot(x,y,'o:',color=color)
    plt.title(title)
    plt.grid(linestyle=':')
    for i in range(len(x)):
        height = y[i]
        plt.text(x[i], height + 0,'%.0f' %height, ha='center', va='bottom', size = 12)
    current_values = plt.gca().get_yticks()
    plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])
    plt.tight_layout()
    plt.show()

plot_maker(sk.index,sk.iloc[:,0],'투자활동현금흐름','#FF7AA2')
plot_maker2(sk.index,sk.iloc[:,1],'ROE','#68CCA9')
plot_maker2(sk.index,sk.iloc[:,2],'PER','#F2DC76')
plot_maker3(sk.index,sk.iloc[:,3],'PBR','#A397C9')

# fig,axes=plt.subplots(2,2)

# axes[0,0].plot(sk.index,sk.iloc[:,0],'o:',color='#FF7AA2')
# axes[0,0].set_title('투자활동현금흐름')
# axes[0,0].grid(linestyle=':')


# axes[0,1].plot(sk.index,sk.iloc[:,1],'o:',color='#68CCA9')
# axes[0,1].set_title('ROE')
# axes[0,1].grid(linestyle=':')


# axes[1,0].plot(sk.index,sk.iloc[:,2],'o:',color='#F2DC76')
# axes[1,0].set_title('PER')
# axes[1,0].grid(linestyle=':')


# axes[1,1].plot(sk.index,sk.iloc[:,3],'o:',color='#A397C9')
# axes[1,1].set_title('PBR')
# axes[1,1].grid(linestyle=':')



# plt.xlabel('연도')
# plt.suptitle('SK하이닉스 2021~2023 주요 재무정보')
# plt.tight_layout()
# plt.show()


