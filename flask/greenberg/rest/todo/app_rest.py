#!flask/bin/python
from flask import Flask, jsonify, abort, request, url_for, make_response, Response
import getopt, sys
from flask_cors import CORS
from oe_debug import print_debug

app = Flask(__name__)
CORS(app)
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
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
#------------------------------------------------------------------------------
@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    elif username == 'omer':
        return 'ruthy'
    return None
#------------------------------------------------------------------------------
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
#------------------------------------------------------------------------------
@app.route('/todo/api/v1.0/tasks/', methods=['GET'])
@auth.login_required
def get_tasks():
    #return jsonify({'tasks': tasks})
    #print_tasks('In get_tasks')
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})
#------------------------------------------------------------------------------
def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task
#------------------------------------------------------------------------------
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})
#------------------------------------------------------------------------------
def print_tasks(header=''):
    print_debug(header)
    try:
        print_debug(('Tasks: {}').format(tasks))
    except Exception as e:
        print_debug (('Error in create_task: {}').format(e))
#------------------------------------------------------------------------------
@app.route('/todo/api/v1.0/tasks/', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    #print_tasks('After create_task')
    return jsonify({'task': task}), 201
#------------------------------------------------------------------------------
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})
#------------------------------------------------------------------------------
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})
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

