import mysql.connector
from mysql.connector import MySQLConnection, Error
############################################################################### 
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost', database='python_mysql', user='root', password='masterkey')
        if conn.is_connected():
            print('Connected to MySQL database')
    except Error as e:
        print(e)
    return conn
############################################################################### 
def query_with_fetchone():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
 
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
############################################################################### 
def query_with_fetchall():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
 
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
############################################################################### 
def update_blob(author_id, filename):
    # read file
    data = read_file(filename)
 
    # prepare update query and data
    query = "UPDATE authors SET photo = %s WHERE id  = %s"
 
    args = (data, author_id)
 
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
############################################################################### 
def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo
############################################################################### 
if __name__ == '__main__':
#    query_with_fetchone()
#    query_with_fetchall()
    update_blob(48, "d:\Omer\Source\Tutorial\MySQL\garth_stein.jpg")