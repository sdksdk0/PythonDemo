__author__ = 'asus'

import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='zp',
                             password='a',
                             db='mysqlforpython',
                             charset='utf8')
try:
    with connection.cursor() as cursor:
        sql="select urlname,urlhref from wikiurl where id is not null "
        count=cursor.execute(sql)
        print(count)

        result=cursor.fetchall()
        print(result)
finally:
    connection.close()
