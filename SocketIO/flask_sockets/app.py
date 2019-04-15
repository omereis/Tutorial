from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import getopt, sys

#------------------------------------------------------------------------------
host = '0.0.0.0'
port = 4000
try:
    if len(sys.argv) > 0:
        print('ARGV      :', sys.argv[1:])
        options, remainder = getopt.getopt(
            sys.argv[1:],
            'h:p:',
            [
            'host=',
            'port='
            ])
except getopt.GetoptError as err:
    print(err) 
    exit(1) 
#------------------------------------------------------------------------------
for opt, arg in options:
    if opt in ('-h', '--host'):
        host = arg.strip();
    elif opt in ('-p', '--port'):
        port = arg.strip();
#------------------------------------------------------------------------------
print('Host: {}'.format(host))
print('Port: {}'.format(port)) 
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': 'got it!'})

if __name__ == '__main__':
    socketio.run(app, host=host, port=port)
