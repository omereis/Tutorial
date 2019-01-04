from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ruth'}
    posts = [
        {
            'author': {'username': 'Joe'},
            'body': 'Cold and dry in DC'
        },
        {
            'author': {'username': 'Inbar'},
            'body': 'Missing my gradparents'
        }
    ]
    return render_template('index.html', posts=posts, user=user)


