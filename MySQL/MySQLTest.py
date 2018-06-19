import mysql
from mysql.connector import MySQLConnection, Error
import os
import MySQLdb
#from python_mysql_dbconfig import 

###############################################################################
def read_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    return data
###############################################################################
def update_blob(id, filename):
    # prepare update query and data
    query = "UPDATE tblBumpsInParams SET in_file_blob = '%s' WHERE id  = %d;"
 
#    db_config = read_db_config()
 
    try:
        data = read_file(filename)
        sql = "INSERT INTO tblBumpsInParams (in_file_blob) VALUES ('%s');"
        q = (sql, (data,))
        conn = ConnectBumpsDB()
        cursor = conn.cursor()
        # read file
#        args = (data, id)
#        conn = MySQLConnection(**db_config)
#        cursor = conn.cursor()
        cursor.execute(q)
#        cursor.execute(query, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
###############################################################################
def ConnectBumpsDB():
    conn = None
    try:
        conn = mysql.connector.connect(host='p858547', database='bumps_db', user='bumps',password='bumps_dba')
    except Error as e:
        print(e)
    return conn
###############################################################################
def NextID(conn,table,field):
    strSql = "select max(%s) from %s;" % (field, table)
#    strSql = "select * from tbl;"
    try:
        conn = ConnectBumpsDB()
        cursor = conn.cursor()
        cursor.execute(strSql)
        strDB = cursor.fetchall()
        id = strDB[0][0] + 1
    except Error as e:
        id = 1
        print(e)
    finally:
        cursor.close()
    return id
###############################################################################
#def update_blob(filename):
###############################################################################
def insert_file(filename):
    # read file
    data = read_file(filename)
    # prepare update query and data
    query = "insert into tblBumpsInParams(in_file_name) values ('%s');" % filename
    try:
        conn = ConnectBumpsDB()
        id = NextID(conn,'tblBumpsInParams','file_id')
        cursor = conn.cursor()
        query = "insert into tblBumpsInParams(in_file_name,file_id) values ('%s',%d);" % (filename, id)
        cursor.execute(query)
#        query = "update tblBumpsInParams set in_file_blob=%s where in_file_name=%s;" % (MySQLdb.escape_string(data), filename)
#        cursor.execute(query)
        conn.commit()
#        update_blob(id,filename)
    except Error as e:
        id = -1
        print(e)
    finally:
        cursor.close()
        conn.close()
    return id
###############################################################################
if __name__ == '__main__':
    try:
        strDir = os.getcwd()
        strFileName = 'D:\\Omer\\Source\\Tutorial\\MySQL\\hdf5_job_outline.png'
        id = insert_file(strFileName)
        if (id > 0):
            update_blob (id, strFileName)
    except Error as e:
        print(e)
