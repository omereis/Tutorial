#!flask/bin/python
#https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
#https://blog.miguelgrinberg.com/post/writing-a-javascript-rest-client

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

def next_task_id ():
    id=0
    for n in range (len(tasks)):
        if 'id' in tasks[n].keys():
            id = max(id, tasks[n]['id'])
    return id + 1

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

def request_data_to_json(msg):
    #print_debug (('request_data_to_json, msg: {}').format(msg))
    msg_str = msg.decode('utf-8')
    #print_debug (('request_data_to_json, msg_str: {}').format(msg_str))
    jsn_msg = eval(msg_str)
    return (jsn_msg)

def complete_record(j_data):
    if ('id' not in j_data.keys()):
        j_data['id'] = tasks[-1]['id'] + 1
    if ('title' not in j_data.keys()):
        j_data['title'] = ""
    if ('description' not in j_data.keys()):
        j_data['description'] = ""
    if ('done' not in j_data.keys()):
        j_data['done'] = False
    return j_data

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    j_data = request_data_to_json (request.data)
    #print_debug(('create_task, j_data: {}').format(j_data))
    try:
        task = {
            'id': tasks[-1]['id'] + 1,
            'done': False
        }
        task['title'] = j_data['title'] if ('title' in j_data) else ""
        task['description'] = j_data['description'] if ('description' in j_data) else ""
        #print_debug(('create_task: title in j_data: {}').format(txt))
    except Exception as e:
        print_debug(('create_task exception: {}').format(e))
    #print_debug(('create_task, task: {}').format(task))
    j_data = complete_record(j_data)
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    j_data = request_data_to_json (request.data)
    if len(task) == 0:
        abort(404)
    task0 = task[0]
    if 'title' in j_data:
        task0['title'] = j_data['title']
    if 'description' in j_data:
        task0['description'] = j_data['description']
    if 'done' in j_data:
        task0['done'] = j_data['done']
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
