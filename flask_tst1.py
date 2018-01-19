import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

@app.route('/')
def index():
    print('running')
    return render_template('template.html', error='too much junk')

@app.route('/')
def show_db_entries():
    print("show_db_entries #1")
#    db = get_db()
#    cur = db.execute('select * from entries order by id desc')
#    blog_entries = cur.fetchall()
    print("show_db_entries #2")
    strLink = "'show_entries.html', entries=blog_entries"
    print ("show_db_entris: %s" % strLink)
    blog_entries = 'blog_entries'
    click = 'clicked'
    return render_template('template.html', error=blog_entries, click_result=click)
#    return render_template('template.html', entries=blog_entries)

@app.route('/table_row')
def my_table_row():
#    if not session:
#        session = SecureCookieSession()
#        print(str(session))
    print ('my_table_row()')
    if session:
        print('session: ' + str(session))
        session['logged_in'] = True
        print ('my_table_row(): wrote to session')
    else:
        print('session is null')
    return redirect (url_for('index'))

@app.route('/on_title_click/<string:param>')
def on_title_click(param):
    print("on_title_click")
    if session.get('logged_in') and param:
        print("logged in")
        try:
            print ("preparing for request")
            blog_entry_id = request.form['id']
            print ("request granted")
            print ("param: %d" % param)
            print ("blog_entry_id: %d" % blog_entry_id)
            db = get_db()
            id = int(param)
            strSql = ('select * from entries where id=%d;' % id)
            cur = db.execute('select * from entries order by id desc')
            blog_entry = cur.fetchall()
            print(strSql)
        except Exception as excp:
            print ("Error:\n" + str(excp.args))
    return redirect(url_for('show_db_entries'))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)
if __name__ == "__main__":
    try:
        app.run (debug=True)
    except Exception as excp:
        print ("Error:\n" + str(excp.args))
