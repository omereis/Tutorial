from mysql.connector import Error
from MyTutorial import connect_bumps
from MySQLTest import NextID
import json
############################################################################### 
if __name__ == '__main__':
#    update_blob(1, "d:\\Omer\\Source\\Tutorial\\MySQL\\garth_stein.jpg")
#    update_blob(2, "d:\\Omer\\Source\\Tutorial\\MySQL\\hdf5_job_outline.png")
#    read_blob(2, "d:\\Omer\\Source\\Tutorial\\MySQL\\blob2.png")
#    save_blob(1,'d:\Omer\Source\Tutorial\MySQL\blob2.png')
    try:
        variable_1 = "HELLO"
        variable_2 = "ADIOS"
        varlist = [variable_1, variable_2]
        conn = connect_bumps()
        id = NextID(conn,'authors','id')

        cursor = conn.cursor()
        myList = [1345,22,3,4,5]
        myList = ['1345','22','3','4','5']
        myListString = str(myList)
        myQuery = "INSERT INTO authors (id,first_name) VALUES (%d,'%s')" % (id, myListString)
        cursor.execute(myQuery)
        conn.commit()

        print("Inserted: '" + myListString + "'")
        myQuery = "select first_name from authors where id=%d;" % id
        cursor.execute(myQuery)
        rec = cursor.fetchone()
        if (rec):
#            value=rec[0]
#            print("value: " + str(value))
            jsonOfBlob = json.loads(rec[0])
            print("retrieved: '" + str(jsonOfBlob) + "'")
            id = id + 1
        else:
            print("rec=None")
#        query = "INSERT INTO authors(id,first_name) VALUES (%d,%r);" % (id,tuple(varlist),)
#        id = id + 1
    except Error as e:
        print("error:\n:" + str(e))
    finally:
        cursor.close()
        conn.close()
