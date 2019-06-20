from flask import Flask
app = Flask(__name__)
from get_host_port import get_host_port

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    host, port = get_host_port()
    print('host={}, port={}'.format(host, port))
    app.run(debug=True, host=host, port=port)
