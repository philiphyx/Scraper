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

MovieName = []
MovieType = []
MovieUrl = []

for i in range(0,150):
    url = 'http://www.ygdy8.net/html/gndy/oumei/list_7_' + str(i+1) + '.html'

    html_data = requests.get(url, timeout=500)
    html_data = html_data.text

    Soup = bs(html_data, 'html.parser')

    for link in Soup.find_all('table', class_='tbspan'):

        z = link.find_all('a')
    #############################################################
        MUrl = z[1].get('href')
        MUrl = 'http://www.ygdy8.net' + MUrl
        MovieUrl.append(MUrl)
    #############################################################
        x = z[1].get_text().encode("latin1").decode("gbk")
        MName = re.compile(r'(?<=《)[^》]+(?=》)')   #去掉书名号，纯文字
        MName = re.search(MName, x).group()
        MovieName.append(MName)
        print(MName)
    ####################
        Mtype = re.compile(r'(?<=年).*(?=《)')
        if (re.search(Mtype, x)):
            Mtype = re.search(Mtype,x).group()      #记得要用group！！
            MovieType.append(Mtype)
        else:
            MovieType.append(0)
#####################################

pd_Movies = pd.Series(MovieName)
pd_Mtype = pd.Series(MovieType)
pd_MovieUrl = pd.Series(MovieUrl)
pd_Movies_All = pd.DataFrame({'Movies_Name': pd_Movies, 'Movies_Type': pd_Mtype,
                                      'Movie_Url': pd_MovieUrl})
pd_Movies_All.to_csv('movies.csv', encoding="utf_8_sig")

    #print(len(MovieName))
          # ,encoding="utf_8_sig"

        ###############################################################



#########################################################