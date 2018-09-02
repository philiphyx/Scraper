# -*- coding: utf-8 -*-
# from urllib import request
import urllib3
import time
import urllib
import re
import sys
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs

#
# url = "https://book.douban.com/tag/python"
# url = "https://book.douban.com/tag/python?start=140&type=T"

from bs4 import BeautifulSoup
import requests
import random

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
# url_ip = 'http://www.xicidaili.com/nn/'
# headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
#     }
# ip_list = get_ip_list(url_ip, headers=headers)
# proxies = get_random_ip(ip_list)
# print(proxies)

##############################################################

url = 'http://www.ygdy8.net/html/gndy/oumei/list_7_2.html'
print(url)
#  proxies=proxies
html_data = requests.get(url,timeout = 500)
html_data = html_data.text
#html_data = html_data.decode('utf-8')
#print(html_data)
#print(html_data)
####################################################################
# res = request.urlopen('https://book.douban.com/subject_search?search_text=python&cat=1001')
# time.sleep(10)
# html_data = res.read().decode('utf-8')
#  soup.find_all("a", class_="sister")
Soup = bs(html_data, 'html.parser')



BookTitle = []
Rates = []
RatePerson = []


for link in Soup.find_all('table', class_='tbspan'):

    z = link.find_all('a')
    #print(z[1])
    x = z[1].get_text().encode("latin1").decode("gbk")
    # content = bytes(x, "UTF-8")
    # content = content.decode("UTF-8")
    # print(content)
    #BookTitle.append(z.get('title'))   #获取属性中的书的名字
    BookTitle.append(x)

print(len(BookTitle))
print(sys.getfilesystemencoding())


###############################################################
pd_Movies = pd.Series(BookTitle)
pd_Movies.to_csv('movies.csv')  #  ,encoding="utf_8_sig"
#DataFrame处理数据
# pd_Rates = pd.Series(Rates,index=[BookTitle])
# pd_RatePerson = pd.Series(RatePerson,index=[BookTitle])
#
# All_Books = pd.DataFrame({'Rates' : pd_Rates,'RatePerson': pd_RatePerson})
#
#
# X = All_Books[All_Books.Rates> 8.0]  #要注意比较的类型！！
# X = All_Books[(All_Books.Rates>7.4) &(All_Books.RatePerson>20)]

