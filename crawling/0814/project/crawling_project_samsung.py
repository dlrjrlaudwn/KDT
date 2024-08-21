import pandas as pd
from bs4 import BeautifulSoup
import collections
if not hasattr(collections,'Callable'):
    collections.Callable=collections.abc.Callable
from selenium import webdriver
import matplotlib.pyplot as plt
import koreanize_matplotlib
from tabulate import tabulate

# cnt=0
# for i in roe:
#     cnt+=1
#     print(cnt)
#     print(i)
#     print('-'*80)

ss_driver=webdriver.Chrome()
ss_driver.get('https://finance.naver.com/item/coinfo.naver?code=006400')

ss_driver.switch_to.frame('coinfo_cp')

ss_html=ss_driver.page_source
bs=BeautifulSoup(ss_html, 'html.parser')

ss_table=bs.find_all('tbody')
ss_row=ss_table[12]
ss_cash=ss_row.find_all('tr')
ss_cash2=ss_cash[1]
ss_roe=ss_cash[21]
ss_per=ss_cash[26]
ss_pbr=ss_cash[28]
ss_cash_flow=ss_cash2.find_all('span',{'class':'cBk'})
ss_roe2=ss_roe.find_all('span',{'class':'cBk'})
ss_per2=ss_per.find_all('span',{'class':'cBk'})
ss_pbr2=ss_pbr.find_all('span',{'class':'cBk'})

ss_c_list=[]
for c in ss_cash_flow:
    ss_c_list.append(c.text)
# print(ss_c_list)

ss_roe_list=[]
for r in ss_roe2:
    ss_roe_list.append(r.text)

ss_p_list=[]
for p in ss_per2:
    ss_p_list.append(p.text)

ss_pbr_list=[]
for p in ss_pbr2:
    ss_pbr_list.append(p.text)

ss_c_dict={'2021':ss_c_list[0],'2022':ss_c_list[1],'2023':ss_c_list[2]}
# print(ss_c_dict)

# print(ss_roe_list)
ss_r_dict={'2021':ss_roe_list[0],'2022':ss_roe_list[1],'2023':ss_roe_list[-2]}
# print(ss_r_dict)

# print(ss_p_list)
ss_p_dict={'2021':ss_p_list[0],'2022':ss_p_list[1],'2023':ss_p_list[-2]}
# print(ss_p_dict)

# print(ss_pbr_list)
ss_pbr_dict={'2021':ss_pbr_list[0],'2022':ss_pbr_list[1],'2023':ss_pbr_list[2]}
# print(ss_pbr_dict)

ss=pd.DataFrame([ss_c_dict,ss_r_dict,ss_p_dict,ss_pbr_dict],index=['영업이익','ROE','PER','PBR'])
ss.loc['영업이익']=ss.loc['영업이익'].str.replace(',','')
ss['2021']=ss['2021'].astype('float')
ss['2022']=ss['2022'].astype('float')
ss['2023']=ss['2023'].astype('float')

ss=ss.T
print(tabulate(ss,headers='keys',tablefmt='psql',numalign='right'))

# fig,axes=plt.subplots(2,2)

# axes[0,0].plot(ss.index,ss.iloc[:,0],color='#FF7AA2')
# axes[0,0].set_title('투자활동현금흐름')

# axes[0,1].plot(ss.index,ss.iloc[:,1],color='#68CCA9')
# axes[0,1].set_title('ROE')

# axes[1,0].plot(ss.index,ss.iloc[:,2],color='#F2DC76')
# axes[1,0].set_title('PER')

# axes[1,1].plot(ss.index,ss.iloc[:,3],color='#A397C9')
# axes[1,1].set_title('PBR')


# plt.xlabel('연도')
# plt.suptitle('삼성SDI 2021~2023 주요 재무정보')
# plt.tight_layout()
# plt.show()

def plot_maker(x,y,title,color):
    plt.plot(x,y,'o-',color=color,linewidth='3.5')
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
    plt.plot(x,y,'o-',color=color,linewidth='3.5')
    plt.title(title)
    plt.grid(linestyle=':')
    for i in range(len(x)):
        height = y[i]
        plt.text(x[i], height + 0.05, '%.2f' %height, ha='center', va='bottom', size = 12)
    current_values = plt.gca().get_yticks()
    plt.gca().set_yticklabels(['{:,.2f}'.format(x) for x in current_values])
    plt.tight_layout()
    plt.show()

def plot_maker3(x,y,title,color):
    plt.plot(x,y,'o-',color=color, linewidth='3.5')
    plt.title(title)
    plt.grid(linestyle=':')
    for i in range(len(x)):
        height = y[i]
        plt.text(x[i], height + 0,'%.2f' %height, ha='center', va='bottom', size = 12)
    current_values = plt.gca().get_yticks()
    plt.gca().set_yticklabels(['{:,.2f}'.format(x) for x in current_values])
    plt.tight_layout()
    plt.show()

plot_maker(ss.index,ss.iloc[:,0],'영업이익','#FF7AA2')
plot_maker2(ss.index,ss.iloc[:,1],'ROE','#68CCA9')
plot_maker2(ss.index,ss.iloc[:,2],'PER','#F2DC76')
plot_maker3(ss.index,ss.iloc[:,3],'PBR','#A397C9')
