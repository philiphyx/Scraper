from urllib import request
import urllib3
import time
import urllib
import re
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs


url = "https://book.douban.com/tag/python"
url = "https://book.douban.com/tag/python?start=140&type=T"
#################################################################
#! /usr/bin/env python3
# import urllib.request
# proxy_support = urllib.request.ProxyHandler({'sock5': 'localhost:1080'})
# opener = urllib.request.build_opener(proxy_support)
# urllib.request.install_opener(opener)
#
# html_data = urllib.request.urlopen("https://book.douban.com/subject_search?search_text=python&cat=1001").read().decode("utf8")
# print(html_data)

#################################################################

# proxy_handler = urllib.request.ProxyHandler({'http': 'http://121.193.143.249:80/'})
# opener = urllib.request.build_opener(proxy_handler)
# html_data = opener.open(url)
# print(html_data.read())


#####################################################
from bs4 import BeautifulSoup
import requests
import random

def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


url_ip = 'http://www.xicidaili.com/nn/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
ip_list = get_ip_list(url_ip, headers=headers)
proxies = get_random_ip(ip_list)
print(proxies)




print(url)
html_data = requests.get(url, headers=headers, proxies=proxies)

html_data = html_data.text

#print(html_data)
####################################################################
# res = request.urlopen('https://book.douban.com/subject_search?search_text=python&cat=1001')
# time.sleep(10)
# html_data = res.read().decode('utf-8')
#  soup.find_all("a", class_="sister")
Soup = bs(html_data, 'html.parser')

#############书名+评论数+评价人数#############################################
# info = Soup.select('#subject_list > ul > li > div.info > h2 > a')
# title = [x.text.strip() for x in info]
# print(title)
# print(len(info))
#
# rate = Soup.select('.rating_nums')
# rate = [x.text.strip() for x in rate]
# print (rate)
# print(len(rate))
#
#
# pl = Soup.select('.pl')
# pinglun = [x.text.strip() for x in pl]
# print (pinglun)
# print(len(pinglun))
##########################################################################
# x = Soup.find_all('li', class_='subject-item')
# print(x[0])
#x = 0
BookTitle = []
Rates = []
RatePerson = []


for link in Soup.find_all('div', class_='info'):

    z = link.find('a')
    BookTitle.append(z.get('title'))   #获取属性中的书的名字
    #BookTitle.append(z.get_text())

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
    if y is None or (y.strip() == ''):  #  有的标签不存在，同上
        y = 0
        RatePerson.append(int(y))
    else:
        #print(y)
        RatePerson.append(int(y))
print(RatePerson)
###############################################################
#结构化数组
# Nparray = np.zeros(20,dtype={'names':('BookTitle','Rates','RatePerson'),
#                    'formats':('U100','i4','i4')})
# Nparray['BookTitle'] = BookTitle
# Nparray['Rates'] = Rates
# Nparray['RatePerson'] = RatePerson
# print(Nparray.dtype)
# print(Nparray['BookTitle'])
# print(Nparray['RatePerson'])

###############################################################
#DataFrame处理数据
pd_Rates = pd.Series(Rates,index=[BookTitle])
pd_RatePerson = pd.Series(RatePerson,index=[BookTitle])
# print(pd_Rates)
# print(pd_RatePerson)
All_Books = pd.DataFrame({'Rates' : pd_Rates,'RatePerson': pd_RatePerson})
#print(All_Books)
#print(All_Books.columns)
#print(All_Books[3:5])   #隐式索引，不包括最后一个索引
# print(All_Books['Rates'])   #两种方式取某一列
# print(All_Books.Rates)
#print(All_Books.values)

X = All_Books[All_Books.Rates> 8.0]  #要注意比较的类型！！
X = All_Books[(All_Books.Rates>7.4) &(All_Books.RatePerson>20)]

#print(X)
#All_Books.to_csv("data.csv",encoding="utf_8_sig")
##############################################################
# print(BookTitle)
# print(len(BookTitle))
# df = pd.DataFrame(RatePerson,columns=['RatePerson','Rates'],index=[BookTitle])
# print(df)
    #print(link.a[title])
    # title = link.find('a')
    # x = title.h2.a
    # print   (x)






# info = Soup.find_all('div', class_='subject-list')
# print(info)
# #comments_content = info[0].find_all('a')
# print(comments_content)
#title = info[0].find_all('a')

#title = title.title
# print(type(comments))
#print(title)

    #comments_content = comments[0].find_all('p')
    # print(type(comments_content))
    # for j in range(0, 15):
    #     text = str(comments_content[j])
    #     f = open('book_name.txt', 'a', encoding='utf-8')
    #     f.write(text)
    #     f.close()

