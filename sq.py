
import sqlite3

if __name__ == "__main__":
    try:
        db = sqlite3.connect("mydb")
        cr = db.cursor()
        cr.execute("create table users(id integer not null primary key, user_name varchar(50))")
        cr.execute("insert into users (id,user_name) values (1, 'user 1')")
        cr.execute("insert into users (id,user_name) values (2, 'user 2')")
        t = cr.execute("select * from users")
        cr.execute ("drop table users")
        db.close()
    except Exception as excp:
        print ("Error:\n" + str(excp.args))
