from flask import Flask, render_template
from data import *

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html', subtitle=subtitle, description=description, tours=tours)

@app.route('/from/<direction>')
def direction_page(direction):
    return render_template('direction.html')

@app.route('/tours/<int:id>')
def tour_page(id):
    return render_template('tours.html', tour=tours.get(id), departures=departures)


app.run()
