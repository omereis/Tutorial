
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.param1 = False

@app.route('/')
def index():
    print('running')
    fAddParam = app.param1
    app.param1 = True
    return render_template('template.html', error='too much junk')

@app.route('/my-link/')
def my_link():
    print('Just got clicked')
    return 'Click'

@app.route('/my-page/<string:user>')
def my_page(user):
    print('Just got clicked')
    print(str(request.form))
    return 'Page for ' + user

@app.route('/table_row')
def my_table_row():
    print ("param1 #1: " + str(app.param1))
    app.param1 = True
    print ("param1 #2: " + str(app.param1))
    print ('my_table_row()')
    return redirect (url_for('index'))
#    return render_template('template.html', click_result='click')
#    return 'redirect'
#    return 'Page for table row'

if __name__ == "__main__":
    try:
        app.run (debug=True)
    except Exception as excp:
        print ("Error:\n" + str(excp.args))
