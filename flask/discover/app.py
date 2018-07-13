# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
#------------------------------------------------------------------------------
# create the application object
app = Flask(__name__)
app.secret_key = 'secret_key'
#------------------------------------------------------------------------------
def login_required(f):
    @wraps(f)
    def wrap (*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Login required')
            return redirect(url_for('login'))
    return wrap
#------------------------------------------------------------------------------
@app.route('/')
@login_required
def home():
    return render_template('index.html')  # render a template
#------------------------------------------------------------------------------
@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')  # render a template
#------------------------------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            session['username']  = 'admin'
            flash ('Just logged in :-)')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
#------------------------------------------------------------------------------
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash ('Just logged out :-(')
    return redirect(url_for('welcome'))
#------------------------------------------------------------------------------
@app.before_first_request
def on_start():
    print("on_start")
    session.clear()
#------------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        session.pop('logged_in', None)
    except Exception as e:
        print("Exception: " + str(e))
    app.run(debug=True, host='0.0.0.0')

