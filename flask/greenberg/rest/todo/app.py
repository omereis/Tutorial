#!flask/bin/python
from flask import Flask, jsonify, abort
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
    }
]
#------------------------------------------------------------------------------
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
#------------------------------------------------------------------------------
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})
#------------------------------------------------------------------------------
if __name__ == '__main__':
    host='127.0.0.1'
    port='5000'
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:p:", ["host", "port"])
        print("no error")
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) 
    for o,a in opts:
        if o in ('-p', '-port'):
            port = a
        elif o in ('-h', '-host'):
            host = a
    app.run(debug=True,host=host,port=port)

