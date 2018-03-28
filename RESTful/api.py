from flask import Flask, request
from flask_restful import Resource, Api

app = Flask (__name__)
api = Api (app)

todos = {}

debug_file = 'd:\\omer\\source\\tutorial\\RESTful\\debug.txt'

class TodoSimple (Resource):
    def get(self,todo_id):
        try:
            return_value = {todo_id: todos[todo_id]}
        except:
            return_value = str(todo_id) + ": no such value"
        try:
            f = open(debug_file, 'a')
            f.write("-----------------------------\n")
            f.write("api.py-TodoSimple.get()\n")
            f.write("todo_id=" + str(todo_id) + "\n")
            f.write("todos =" + str(todos) + "\n")
            f.write("todos[todo_id]=" + str(return_value) + "\n")
        finally:
            f.close()
        return {todo_id: return_value}
#        return {todo_id:todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        try:
            return_value = {todo_id: todos[todo_id]}
        except:
            return_value = str(todo_id) + ": no such value"
        try:
            f = open(debug_file, 'a')
            f.write("-----------------------------\n")
            f.write("api.py-TodoSimple.post()\n")
            f.write("todo_id=" + str(todo_id) + "\n")
            f.write("todos =" + str(todos) + "\n")
            f.write("todos[todo_id]=" + str(todos[todo_id]) + "\n")
        finally:
            f.close()
        return {todo_id: return_value}
#        return {todo_id: todos[todo_id]}

api.add_resource (TodoSimple, '/<string:todo_id>')
#api.add_resource (TodoSimple, '/<string:todo_id>')

if (__name__ == '__main__'):
    try:
        f = open(debug_file, 'a')
        f.write("-----------------------------\n")
        f.write("api.py-__name__ is __main\n")
    finally:
        f.close()
    app.run(debug=True)