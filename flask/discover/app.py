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
# use decorators to link the function to a url
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
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
