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
def connect_bumps():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost', database='bumps_db', user='bumps', password='bumps_dba')
        if conn.is_connected():
            print('Connected to BUMPS database')
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
    try:
        query = "UPDATE tblBumpsInParams SET in_file_blob = %s WHERE file_id  = %s"
        args = (data, author_id)
        conn = connect_bumps()
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
############################################################################### 
def save_blob(blob_id ,filename):
    try:
        query = "select in_file_blob from tblbumpsinparams where file_id=%S;"
        conn = connect_bumps()
        cursor = conn.cursor()
        cursor.execute(query, (blob_id,))
        blob_file = cursor.fetchone()[0]
        write_file(blob_file, filename)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
############################################################################### 
def read_blob(author_id, filename):
    # select photo column of a specific author
    query = "SELECT photo FROM authors WHERE id = %s"
 
    try:
        # query blob data form the authors table
        conn = connect()
        cursor = conn.cursor()
        sql = query % author_id
        cursor.execute(query, (author_id,))
        record = cursor.fetchone()

        cursor.execute(sql)
        record = cursor.fetchone()
#        photo = cursor.fetchone()[0]

        cursor.close()
        conn.close()
        conn = connect_bumps()
        cursor = conn.cursor()
        sql = "SELECT in_file_name FROM tblbumpsinparams where file_id=%d;" % author_id
        cursor.execute(sql)
        record = cursor.fetchone()
        data = None
        if record:
            data = record[0]
            print("Record fetched: " + data)
        else:
            print("Record is NULL")

        sql = "SELECT in_file_blob FROM tblbumpsinparams where file_id=%d;" % author_id
        cursor.execute(sql)
        record = cursor.fetchone()
        if record:
            data = record[0]
            write_file(data, filename)
            print("Record fetched")
        else:
            print("Record is NULL")

        # write blob data into a file
#        write_file(photo, filename)
 
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
def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
############################################################################### 
if __name__ == '__main__':
#    query_with_fetchone()
#    query_with_fetchall()
    update_blob(1, "d:\Omer\Source\Tutorial\MySQL\garth_stein.jpg")
    update_blob(2, "d:\Omer\Source\Tutorial\MySQL\hdf5_job_outline.png")
    read_blob(2, "d:\\Omer\\Source\\Tutorial\\MySQL\\blob2.png")
    save_blob(1,'d:\Omer\Source\Tutorial\MySQL\blob2.png')
