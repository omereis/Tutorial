import mysql.connector
from mysql.connector import MySQLConnection, Error
import datetime
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
#------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------
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
#        conn = connect()
        conn = mysql.connector.connect(host='localhost', database='python_mysql', user='root', password='masterkey')
        cursor = conn.cursor()
        query = "select * from authors where id = %s;" % author_id
        cursor.execute(query)
        res = cursor.fetchone()
        print ("Author %d: %s %s" % (author_id,res[1],res[2]))
        query = "UPDATE authors SET photo = %s WHERE id  = %s"
#        query = "UPDATE tblBumpsInParams SET in_file_blob = %s WHERE file_id  = %s"
#        strSql = query % (data, author_id)
        args = (data, author_id)
        cursor.execute(query, args)
#        cursor.execute(strSql)
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
#------------------------------------------------------------------------------
def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo
#------------------------------------------------------------------------------
def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
#------------------------------------------------------------------------------
def save_list():
    some_list = ['this', 'that', 'some', 'other', 'thing']
    try:
        conn = connect()
        cursor = conn.cursor()
        results = db.executemany('INSERT INTO tbl (str) VALUES (?)', [(x,) for x in some_list])
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
#------------------------------------------------------------------------------
def select_author(id):
    try:
        conn = mysql.connector.connect(host='localhost', database='python_mysql', user='root', password='masterkey')
#        conn = mysql.connector.connect(host='ncnr-r9nano', database='bumps_db', user='bumps', password='bumps_dba')
        cursor = conn.cursor()
        query = "select * from authors where id=%s;" % id
#        query = "select * from tbl_authors where id = %s;" % id
        cursor.execute(query)
        res = cursor.fetchall()
        print (("author %s: " % id) + str(res[0][1] + " " + res[0][2]))
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
#------------------------------------------------------------------------------
TABLE_PARAMS      = "t_bumps_jobs"

FIELD_TOKEN       = 'token'
FIELD_JOB_ID      = 'job_id'
FIELD_TIME_START  = 'time_started'
FIELD_PARAMS      = 'params'
FIELD_CONTENT     = 'in_file_content'
FIELD_TIME_ENDED  = 'time_ended'
FIELD_RES_DIR     = 'result_dir'
FIELD_RES_CONTENT = 'result_zip'
#------------------------------------------------------------------------------
def get_current_time_string():
    strTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return (strTime)
#------------------------------------------------------------------------------
def insert_result (token, job_id, zip_file_name):
    try:
        zip_data = read_file (zip_file_name)
        str_end_time = get_current_time_string()
        conn = mysql.connector.connect(host='ncnr-r9nano', database='bumps_db', user='bumps', password='bumps_dba')
        cursor = conn.cursor()
        strWhere =  " where (%s='%s' and %s=%s);" % (FIELD_TOKEN, str(token), FIELD_JOB_ID, str(job_id))
        cursor.execute("update %s set %s='%s' %s" %  (TABLE_PARAMS, FIELD_TIME_ENDED, str_end_time, strWhere))
        conn.commit()
        query= "update %s set %s=%%s %s;" %  (TABLE_PARAMS, FIELD_RES_CONTENT, strWhere)
#        query= "update t_bumps_jobs set result_zip=%%s %s" %  ()
        args = (zip_data, strWhere)
        cursor.execute(query, (zip_data, ))
#        cursor.execute(query, args)
        conn.commit()
        print("Token '%s', Job ID %d, blob updated" % (str(token), job_id))
    except Error as e:
        print(e)
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()
        conn.close()
#------------------------------------------------------------------------------
if __name__ == '__main__':
    select_author(2)
#    select_author(12)
    update_blob(1, "d:\\Omer\\Source\\Tutorial\\MySQL\\garth_stein.jpg")
    update_blob(2, "d:\\Omer\\Source\\Tutorial\\MySQL\\blob2.png")
    insert_result ('0c5447', 1, "d:\\Omer\\Source\\Tutorial\\MySQL\\test.zip")
#    update_blob(2, "d:\\Omer\\Source\\Tutorial\\MySQL\\hdf5_job_outline.png")
#    read_blob(2, "d:\\Omer\\Source\\Tutorial\\MySQL\\blob2.png")
#    save_blob(1,'d:\Omer\Source\Tutorial\MySQL\blob2.png')
#    save_list()
