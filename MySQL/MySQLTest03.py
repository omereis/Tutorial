import mysql
from mysql.connector import MySQLConnection, Error
#import os
#import MySQLdb

try:
    conn = mysql.connector.connect(host='p858547', database='bumps_db', user='bumps',password='bumps_dba')
    cursor = conn.cursor()
    strSql = "select * from tbl;"
    cursor.execute(strSql)
    strDB = cursor.fetchall()
    print(strDB)
except Error as e:
    print(e)
finally:
    cursor.close()
    conn.close()
