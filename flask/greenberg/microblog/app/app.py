from . import app
app.secret_key = 'secret_key'
if __name__ == '__main__':
    try:
        session.pop('logged_in', None)
    except Exception as e:
        print("Exception: " + str(e))
    app.run(debug=True, host='0.0.0.0')
