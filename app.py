from flask import Flask
from data import *

app = Flask(__name__)

@app.route('/')
def main_page():
    return '<h2>KEKW</h2>'

@app.route('/from/<direction>')
def direction():
    return "direction"

@app.route('/tours/<id>')
def tours():
    return "tours"
print(title)

app.run()