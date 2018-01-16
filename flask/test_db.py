import os
import sqlite3

def testdb ():
    try:
        fname = os.environ['FLASKR_DATABASE']
        db = sqlite3.connect(fname)
        cr = db.cursor()
        cr.execute("select * from entries;")
        rows = cr.fetchall()
        db.close()
        print ("Database closed")
    except Exception as excp:
        print ("Error:\n" + str(excp.args))

testdb ()
