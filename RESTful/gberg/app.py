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
    jsn = msg.decode('utf-8')
    s=jsn[jsn.find('{')+1:jsn.find('}')]
    s_split=s.split(':')
    jsn_src = '{"'+s_split[0]+'":"'+s_split[1]+'"}'
    j_data = json.loads(jsn_src)
    return j_data

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
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': j_data['title'],
        'description': "",
        'done': False
    }
    j_data = complete_record(j_data)
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    print_debug('task_id: ' + str(task_id))
    task = [task for task in tasks if task['id'] == task_id]
    print_debug('task: ' + str(task))
    if len(task) == 0:
        abort(404)
    #if not request.json:
        #abort(400)
    print_debug('request data: ' + str(request.data))
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


if __name__ == '__main__':
    app.run(debug=True, port=5001)
