__author__ = 'asus'
from urllib.request import urlopen
from bs4 import  BeautifulSoup
import re
import pymysql


resp=urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")

soup=BeautifulSoup(resp,"html.parser")

listUrls=soup.findAll("a",href=re.compile("^/wiki/"))

for url in listUrls:
    if not re.search("\.(jpg|JPG$)",url["href"]):
        print(url.get_text(),"<-->",url["href"])

connection = pymysql.connect(host='localhost',
                             user='zp',
                             password='a',
                             db='mysqlforpython',
                             charset='utf8')
try:
    with connection.cursor() as cursor:
        for url in listUrls:
            sql = "insert into `wikiurl`(`urlname`,`urlhref`)values(%s,%s)"
            cursor.execute(sql,(url.get_text(),"http://baike.so.com"+url["href"]))
            connection.commit();
finally:
    connection.close();
#print(soup)

#print(listUrls)