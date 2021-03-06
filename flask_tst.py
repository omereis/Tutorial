import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def show_db_entries():
    if session:
        print(str(session))
    else:
        print ("session is null")
    if session.get('logged_out'):
        db = get_db()
        cur = db.execute('select * from entries order by id desc')
        blog_entries = cur.fetchall()
    print("show_db_entries")
    strLink = "'show_entries.html', entries=blog_entries"
    return render_template('template.html', message=strLink)
#    return render_template('show_entries.html', entries=blog_entries)
#    return render_template(strLink)

@app.route('/add', methods=['POST'])
def add_entry():
    print("add_entry()")
#    if not session.get('logged_in'):
#        abort(401)
#    db = get_db()
    strSql = "insert into entries (title, entry_text) values ('%s', '%s');" % \
                (request.form['title'], request.form['blog_text'])
#    db.execute(strSql)
#    db.commit()
#    flash('New entry was successfully posted')
    print("add_entry: sql insert: " + strSql)
    return redirect(url_for('show_db_entries'))

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash(app.config['USERNAME'] + ': You were logged in')
            return redirect(url_for('show_db_entries'))
        flash('NOT logged in')
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_db_entries'))

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='deep',
    PASSWORD='purple'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/table_row', methods=['POST'])
def my_table_row():
    print ('my_table_row()')
#    firstname
    if (request.method == 'POST'):
        print("POST method")
    else:
        print("NOT POST method")
    print ('my_table_row(): request=:' + request)
    print ('my_table_row(): request.form=:' + request.form)
#    print ('my_table_row(): len(request.form)=: + len(request.form))
    return redirect (url_for('show_db_entries'))

if __name__ == "__main__":
    try:
        x = app.config.get('JWT_ACCESS_TOKEN_EXPIRES')
        y = 1
        app.run (debug=True)
    except Exception as excp:
        print ("Error:\n" + str(excp.args))
