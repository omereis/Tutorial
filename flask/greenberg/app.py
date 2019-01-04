#!flask/bin/python
from flask import Flask, jsonify, abort, request, url_for, make_response, Response
import getopt, sys

app = Flask(__name__)
#------------------------------------------------------------------------------
@app.route('/')
def index():
    return "Hello, World!"
#------------------------------------------------------------------------------
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    },
    {
        'id': 3,
        'title': u'Learn REST',
        'description': u'Complete Greenberg''s tutorial', 
        'done': False
    }
]
#------------------------------------------------------------------------------
if __name__ == '__main__':
    host='127.0.0.1'
    port='5000'
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:p:", ["host", "port"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) 
    for o,a in opts:
        if o in ('-p', '-port'):
            port = a
        elif o in ('-h', '-host'):
            host = a
    app.run(debug=True,host=host,port=port)



