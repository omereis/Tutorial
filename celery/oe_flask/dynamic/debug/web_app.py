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
app.config['MAIL_USERNAME'] = os.environ.get('one4')
app.config['MAIL_PASSWORD'] = os.environ.get('Haimes1960)@')
app.config['MAIL_DEFAULT_SENDER'] = 'flask@example.com'

# Celery configuration
app.config['BROKER_URL']  = "amqp://rabbit-server"
app.config['BACKEND_URL'] = "redis://redis-server"
'''
try:
    f = open ('oe_debug.txt', "w")
    f.write ("celery setup\n")
    f.write ("app.config['BROKER_URL'] = " + app.config['BROKER_URL'] + "\n")
    f.close
except Exception as excp:
    print ("Error:\n" + str(excp.args))
'''
# Celery configuration
app.config['BROKER_URL']  = get_environ_var ('BROKER_URL', 'redis://localhost:6379/0')
app.config['BACKEND_URL'] = get_environ_var ('BACKEND_URL', 'redis://localhost:6379/0')

# Initialize extensions
debug_msg = ""
try:
    mail = Mail(app)
    debug_msg = "mail initiated"
except Exception as excp:
    debug_msg = str(excp.args)

# Initialize Celery
try:
    celery = Celery(app.name, broker=app.config['BROKER_URL'], backend=app.config['BACKEND_URL'])
    celery.conf.update(app.config)
    debug_msg = "celery initiated"
except Exception as excp:
    debug_msg = str(excp.args)
@app.route('/1')
def hello_world():
    return 'Web App:<br>Flask Dockerized'

@celery.task
def send_async_email(msg):
    """Background task to send an email with Flask-Mail."""
    try:
        f = open ('oe_debug.txt', "w")
        f.write ("\ninside 'send_async_email'\n")
        f.write ("msg = " + str(msg) + "'\n")
        f.close()
    except Exception as excp:
        print ("Error:\n" + str(excp.args))
    with app.app_context():
        mail.send(msg)


@celery.task(bind=True)
def long_task(self):
    """Background task that runs a long function with progress reports."""
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10, 50)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective),
                                              random.choice(noun))
        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': total,
                                'status': message})
        time.sleep(1)
    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': 42}

'''
        try:
            f = open ('oe_debug.txt', "a+")
            f.write("index(), line #84\n")
            f.write('method = ' + method + '\n')
            f.close
        except Exception as excp:
            print ("Error:\n" + str(excp.args))
'''
@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        f = open ('oe_debug.txt', "a+")
        f.write("index(), line #90\n")
        if 'method' in locals():
            f.write('method = ' + method + '\n')
        else:
            f.write('method undefined\n')
        f.close()
    except Exception as excp:
        print ("Error:\n" + str(excp.args))
       
    if request.method == 'GET':
        return render_template('index.html', email=session.get('email', ''))
    email = request.form['email']
    session['email'] = email

    # send the email
    msg = Message('Hello from Flask',
                  recipients=[request.form['email']])
    msg.body = 'This is a test email sent from a background Celery task.'
    try:
        f = open ('oe_debug.txt', "a+")
        f.write("index(), line #100\n")
        f.write ('email = ' + email + "'\n")
        if 'method' in locals():
            f.write('method = ' + method + '\n')
        else:
            f.write('line #129, method undefined\n')
        f.close()
    except Exception as excp:
        print ("Error:\n" + str(excp.args))
    if request.form['submit'] == 'Send':
        # send right away
        f = open ('oe_debug.txt', "a+")
        f.write("ended up here: line 136, before calling 'send_async_email.delay'\n")
        f.close()
#        send_async_email.delay(msg)
        send_async_email(msg)
        flash('Sending email to {0}'.format(email))
    else:
        # send in one minute
        f = open ('oe_debug.txt', "a+")
        f.write("ended up here: line 140, before calling 'send_async_email'\n")
        f.close()
        send_async_email.apply_async(args=[msg], countdown=60)
        flash('An email will be sent to {0} in one minute'.format(email))

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

