from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/showdown')
def showdown():
    return render_template('showdown.html')