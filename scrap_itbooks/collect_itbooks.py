#http://www.allitebooks.org/page/7/?s=python

from urllib import request
from common_lib import get_agent
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import time

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

timeStamp = time.strftime("%y%m%d_%H_%M_%S", time.localtime())
keyWord = input("please input your keywords")

res = requests.get('http://www.allitebooks.org/page/1/?s=' + str(keyWord), timeout=30, headers=get_agent())

html_data = res.text

Soup = bs(html_data, 'html.parser')

lastPage = Soup.find('a', title='Last Page →')
lastPage = int(lastPage.text) if lastPage else 1


print("total page is ",lastPage)
bookTitle = []
bookAuthor = []
bookURL = []

# http://www.allitebooks.org/page/1/?s=python
for i in range(1, lastPage+1):
    html_data = requests.get("http://www.allitebooks.org/page/" + str(i) + "/?s=" + str(keyWord), timeout=30, headers=get_agent())
    html_data = html_data.text
    Soup = bs(html_data, 'html.parser')
    print("start to scrap %d page", i)

    for link in Soup.find_all('div', class_='entry-body'):

        title = link.find('a', rel="bookmark")
        bookTitle.append(title.text)

        author = link.find('a', rel="tag")
        bookAuthor.append(author.text if author else None)

        bookURL.append(link.find('a', rel="bookmark").get('href'))


# pd_bookTitleL = pd.Series(bookTitle, index=[bookTitle])
pd_bookURL = pd.Series(bookURL, index=[bookTitle])
pd_bookAuthor = pd.Series(bookAuthor, index=[bookTitle])
# print(pd_bookURL)
#
# print(pd_bookAuthor)
# df_book = pd.DataFrame(bookTitle, bookAuthor, bookURL, index=bookTitle)
All_Books = pd.DataFrame({'Book Author': bookAuthor,'URL': pd_bookURL})
#
All_Books.to_csv("data_itBooks" + str(timeStamp) + "_" + str(keyWord) + ".csv")
