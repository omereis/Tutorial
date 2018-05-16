import os
import random
import time
from flask import Flask, request, render_template, session, flash, redirect, \
    url_for, jsonify
from flask.ext.mail import Mail, Message
from celery import Celery
#from flask import Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = 'top-secret!'

def get_environ_var (key, default_value):
    result_value = ""
    try:
        result_value = os.environ.get (key)
    except:
        result_value = default_value
    return result_value

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'flask@example.com'

# Celery configuration
app.config['BROKER_URL']  = get_environ_var ('BROKER_URL', 'redis://localhost:6379/0')
app.config['BACKEND_URL'] = get_environ_var ('BACKEND_URL', 'redis://localhost:6379/0')


# Initialize extensions
mail = Mail(app)

# Initialize Celery
celery = Celery(app.name, broker=app.config['BROKER_URL'], backend=app.config['BACKEND_URL'])
celery.conf.update(app.config)

try:
    f = open ('oe_debug.txt', "a+")
    f.write("app.config['BROKER_URL']: " + app.config['BROKER_URL'])
    f.close
except Exception as excp:
    print ("Error:\n" + str(excp.args))

@app.route('/1')
def hello_world():
    return 'Web App:<br>Flask Dockerized'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', email=session.get('email', ''))
    email = request.form['email']
    session['email'] = email

    # send the email
    msg = Message('Hello from Flask',
                  recipients=[request.form['email']])
    msg.body = 'This is a test email sent from a background Celery task.'
    if request.form['submit'] == 'Send':
        # send right away
        send_async_email.delay(msg)
        flash('Sending email to {0}'.format(email))
    else:
        # send in one minute
        send_async_email.apply_async(args=[msg], countdown=60)
        flash('An email will be sent to {0} in one minute'.format(email))

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

