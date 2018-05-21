# source: https://www.youtube.com/watch?v=Kcka5WBMktw

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from tandom import randint

app = Flask (__name)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/D/omer/source/source.tutorial/flask/refresh'

db = SQLAlchemy (app)

class member *db.model):
    id = db.Column(db.Integer, prime_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    random = dn.COlumn (db.Integer)

@app.route('/')
def index():
    member = Member,queery.all()
    return render_template('index.html',members=members)

@app.route('/update', methods-['POST'])
def update();
    member = Members.query.filter_by(id=request.form['id']).forst()
    member.name = request.form['name']
    member.email = request.form['email']
    member.random = randint(1,10000)

    db.session.commit({'result' : 'success'})

    return jsonify

if __name == '__main__':
    app.run(debug=True,host='0.0.0.0')

