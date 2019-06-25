from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import json
# Source:
# https://stackoverflow.com/questions/40963401/flask-dynamic-data-update-without-reload-page
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/suggestions')
def suggestions():
    text = request.args.get('jsdata')
    test_text = request.args.get('tstdata')
    print(f'suggestions, text: {text}')
    try:
        print(f'content of request.args.get is {dir(request.args.get)}')
        print(f'type of request.args.get is {type(request.args.get)}')
        print(f'Test text: "{test_text}"')
    except Exception as e:
        print(f'suggestions, error: {e}')
    suggestions_list = []

    if text:
        r = requests.get('http://suggestqueries.google.com/complete/search?output=toolbar&hl=ru&q={}&gl=in'.format(text))

        soup = BeautifulSoup(r.content, 'lxml')

        suggestions = soup.find_all('suggestion')

        for suggestion in suggestions:
            suggestions_list.append(suggestion.attrs['data'])

        #print(suggestions_list)
    return render_template('suggestions.html', input_text='test_text')
    #return render_template('suggestions.html', input_text='test_text')
    #return render_template('suggestions.html', suggestions=suggestions_list, input_text=test_text)
@app.route('/onsendclick')
def on_send_click():
    res = {}
    try:
        res['alg'] = request.args.get('algorithm')
        res['stp'] = request.args.get('steps')
        res['brn'] = request.args.get('burn')
    except Exception as e:
        print(f'Run time error in "on_send_click": {e}')
    res_txt = json.dumps(res)
    return res_txt
    #render_template('suggestions.html', input_text=res_txt)

if __name__ == '__main__':
    app.run(debug=True)