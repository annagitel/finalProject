"""
Main program run file


"""
import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/dashboard')
@app.route('/')
def dashboard():
    with open('data.json', 'r') as f:
        data = json.loads(f.read())
    print(type(data))
    return render_template(
        'dashboard.html',
        data=data
    )


'''
if __name__ == '__main__':
    api_data = {'brtfrc': [{},{},{},{}], 'dos': [{},{},{},{}], 'jsonjctn': [{},{},{},{}], 'xss': [{},{},{},{}]}
'''
