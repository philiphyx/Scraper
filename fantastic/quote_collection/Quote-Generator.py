# from twilio.rest import TwilioRestClient
from time import sleep

import requests

import json
import sqlite3
import re

import argparse


# account_sid = " <Your sid> "
# auth_token = " <Your auth_token> "
#
# ourNumber = " <Your number> "
def getQuotesFromApi():
    requestParams = {
        "method": "getQuote",
        "key": "457653",
        "format": "json",
        "lang": "en"
    }
    url = "http://api.forismatic.com/api/1.0/"

    requestToApi = requests.post(url, params=requestParams)  # Requests the qoute from the API
    print(requestToApi)
    json = requestToApi.json()  # This grabs the data from the response from API
    # print(json)
    # finishedQuote = json['quoteText'] + " -" + json['quoteAuthor']  # The finished quote!

    dict = {'quoteText':json['quoteText'],'quoteAuthor':json['quoteAuthor']}
    print(dict)
    return dict

def connectDB():
    conn = sqlite3.connect('C:/Users/PhilipHuang/PycharmProjects/Scraper/fantastic/db.sqlite3')
    return conn

def insertIntoDB(conn, data):
    # conn = sqlite3.connect('C:/Users/PhilipHuang/PycharmProjects/Scraper/fantastic/db.sqlite3')
    # print('quote is : ',data['quoteText'])
    print('Author is : ', data['quoteAuthor'])
    # print(data['quoteAuthor'])
    if ( not data['quoteAuthor'] ):
        data['quoteAuthor'] = 'Unknown'

    # sql = "insert into quotes(quoteText,quoteAuthor) values('%s','%s')" % (data['quoteText'], data['quoteAuthor'])
    sql = "insert into flights_quotes(quoteText,quoteAuthor) values('%s','%s')" % (data['quoteText'], data['quoteAuthor'])
    print(sql)

    try:
        print('insert quote data')
        conn.execute(sql)
        conn.commit()
        print('Complete inserting')
        # conn.close()
    except sqlite3.Error as e:
        print(e)


conn = connectDB()

for i in range(10000):
    try :
        data = getQuotesFromApi()
        insertIntoDB(conn, data)
        sleep(3)
    except Exception as e:
        print(e)
    continue


    # insertIntoDB(conn, data)
    # sleep(7)
conn.close()