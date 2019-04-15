from flask import Flask
import getopt, sys

#------------------------------------------------------------------------------
host = '0.0.0.0'
port = 4000
#------------------------------------------------------------------------------
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
# Basic Flask Python Web App
print("Host: {}", format(host));
print("Port: {}", format(port));
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()