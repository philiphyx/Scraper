#add  comment first line

from urllib import request
import urllib3
import time
import urllib
import re
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup
import requests
import random
############################
#   this is a git hub test for first time
#url = "https://book.douban.com/tag/python"
#url = "https://book.douban.com/tag/python?start=160&type=T"


#####################################################################
# def get_ip_list(url, headers):
#     web_data = requests.get(url, headers=headers)
#     soup = BeautifulSoup(web_data.text, 'lxml')
#     ips = soup.find_all('tr')
#     ip_list = []
#     for i in range(1, len(ips)):
#         ip_info = ips[i]
#         tds = ip_info.find_all('td')
#         ip_list.append(tds[1].text + ':' + tds[2].text)
#     return ip_list
#
# def get_random_ip(ip_list):
#     proxy_list = []
#     for ip in ip_list:
#         proxy_list.append('http://' + ip)
#     proxy_ip = random.choice(proxy_list)
#     proxies = {'http': proxy_ip}
#     return proxies
#
#
# url_ip = 'http://www.xicidaili.com/nn/'
# headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
#     }
# ip_list = get_ip_list(url_ip, headers=headers)
# proxies = get_random_ip(ip_list)
# print(proxies)
#####################################################################
BookTitle = []
Rates = []
RatePerson = []
BookUrl = []

for i in range(0,20):
#url = "https://book.douban.com/tag/python?start=160&type=T"
    # html_data = requests.get("https://book.douban.com/tag/概率?start="+ str(
    #     20 * i) + "&type=S", headers=headers, proxies=proxies)
    html_data = requests.get("https://book.douban.com/tag/概率?start="+ str(
        20 * i) + "&type=S")
    html_data = html_data.text
    Soup = bs(html_data, 'html.parser')

    for link in Soup.find_all('div', class_='info'):

        z = link.find('a')
        BookTitle.append(z.get('title'))  #获取属性中的书的名字
        #BookTitle.append(z.get_text())
        BookUrl.append(z.get('href'))

    #评价的星级
        x = link.find('span',class_="rating_nums")

        # 搜不到为空要这么写！！！也有可能是有这个标签但是为空的情况
        if x is None or (x.text.strip() == ''):
            x = 0
            #print('001  ' + str(x))
            Rates.append(float(x))
        else:
            #print(x.text)
            #x = re.sub("\D", "", x.text)   #不可以用 会把小数点去掉
            x = re.sub('~(\d+(\.\d+)?)',"",x.text)  #去掉 非！！数字或者小数
            #print('002  ' + x)
            Rates.append(float(x))
    #评论人数
        y = link.find('span',class_="pl")
        #不是数字的都替代为空
        y = re.sub("\D", "", y.text)
        if y is None or  (y == '10') or (y.strip() == ''):  # 有的标签不存在，同上
            y = 0
            RatePerson.append(int(y))
        else:
            # print(y)
            RatePerson.append(int(y))
    print("第"+ str(i+1) + "页爬取完毕...")

print("爬取完成！！！")
    #DataFrame处理数据
pd_Rates = pd.Series(Rates,index=[BookTitle])
pd_RatePerson = pd.Series(RatePerson,index=[BookTitle])
pd_BookUrl = pd.Series(BookUrl,index=[BookTitle])

    # print(pd_Rates)
    # print(pd_RatePerson)
All_Books = pd.DataFrame({'Rates' : pd_Rates,'RatePerson': pd_RatePerson,'Book_Url':pd_BookUrl})


#print(All_Books.dropna().describe())
#print(All_Books.groupby('Rates').sum())
    #print(All_Books)
    #print(All_Books.columns)
    #print(All_Books[3:5])   #隐式索引，不包括最后一个索引
    # print(All_Books['Rates'])   #两种方式取某一列
    # print(All_Books.Rates)
    #print(All_Books.values)
# X = All_Books[All_Books.Rates> 8.0]  #要注意比较的类型！！
X= All_Books[(All_Books.Rates>7.9) &(All_Books.RatePerson>100)]
X = X.sort_values(by = ['Rates'],axis = 0,ascending = False)
# print(X)
X.to_csv("data.csv",encoding="utf_8_sig")
    ##############################################################