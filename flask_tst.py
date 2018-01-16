from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    print('running')
    return render_template('template.html')

@app.route('/my-link/')
def my_link():
    print('Just got clicked')
    return 'Click'

if __name__ == "__main__":
    try:
        app.run (debug=True)
    except Exception as excp:
        print ("Error:\n" + str(excp.args))
