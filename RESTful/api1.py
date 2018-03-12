from flask import Flask
from flask_restful import Resource, Api

app = Flask (__name__)
api = Api (app)

debug_file = 'd:\\omer\\source\\tutorial\\RESTful\\ldebug1.txt'

class HelloWorld (Resource):
    def get(self):
        try:
            f = open(debug_file, 'a')
            f.write("-----------------------------\n")
            f.write("api1.py-TodoSimple.get()\n")
        finally:
            f.close()
        return {'Hello': 'World'}

api.add_resource (HelloWorld, '/')

if (__name__ == '__main__'):
    app.run(debug=True)