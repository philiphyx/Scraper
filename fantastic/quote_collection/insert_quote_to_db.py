import sqlite3   #导入模块

#conn = sqlite3.connect('example.db') #连接数据库
# connect()方法，可以判断一个数据库文件是否存在，如果不存在就自动创建一个，如果存在的话，就打开那个数据库。

#再创建一个Cusor对象，并且调用Cursor对象的execute()方法来执行SQL语句创建数据表以及查询、插入、修改或删除数据库中的数据，例如：
#c = conn.cursor()

#创建表
#c.execute('''CREATE TABLE stocks(date text,trans text,symbol text,gty real,price real)''')

#向表中插入一条数据
#c.execute('''insert into stocks values('2016-01-05','BUY','RHAT',100,35.14)''')

#提交当前事务，保存数据
#conn.commit()

#关闭数据库连接
#conn.close()



#查询刚才插入的数据
#由于刚才已经关闭了数据库连接，需要重新创建Connection对象和Cursor对象
conn = sqlite3.connect('C:/Users/PhilipHuang/PycharmProjects/Scraper/fantastic/db.sqlite3')
c = conn.execute('''select * from quotes''')
print(c)   #<sqlite3.Cursor object at 0x00000000007E25E0>

print(list(c))   #[('2016-01-05', 'BUY', 'RHAT', 100.0, 35.14)]

#数据成功提取出来了