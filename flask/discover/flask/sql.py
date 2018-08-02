import mysql
from mysql.connector import MySQLConnection, Error
import os, time, datetime 

try :
    conn = mysql.connector.connect(host='ncnr-r9nano.campus.nist.gov', database='lite', user='discover',password='flask')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posts (title,description) VALUES("Good", "I\'m good.")')
    cursor.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    cursor.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
    cursor.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')
    conn.commit()
except Exception as e:
    print("Exception: '%s'" % str(e))
finally:
    cursor.close()
    conn.close()