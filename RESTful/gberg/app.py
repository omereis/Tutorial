#!flask/bin/python

from flask import Flask, jsonify, render_template, redirect, url_for, request, abort, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    return "Hello, World!"

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
        'title': u'Learn RESTful',
        'description': u'Need to connect front end to bumps backend', 
        'done': False
    }
]

from oe_debug import print_debug

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'tasks': tasks})
        #abort(404)
    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

import datetime, json

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    msg = request.data
    jsn = msg.decode('utf-8')
    print_debug(('jsn: {}').format(jsn))
    s=jsn[jsn.find('{')+1:jsn.find('}')]
    s_split=s.split(':')
    jsn_src = '{"'+s_split[0]+'":"'+s_split[1]+'"}'
    print_debug("jsn_src: " + str(jsn_src))
    j_data = json.loads(jsn_src)
    print_debug("j_data: " + str(j_data))
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': j_data['title'],
        'description': "",
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)
