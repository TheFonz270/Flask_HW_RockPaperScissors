from app import app
from flask import render_template, redirect, request
from models.player import Player, players
# from models.play_test import players

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    return render_template('play.html', players = players)

@app.route('/player1', methods=['POST'])
def player1():
    print (request.form)
    name = request.form['name']
    choice = request.form['choice']
    player1 = Player(name, choice)
    Player.add_player_to_players(player1)
    return redirect('/play')

@app.route('/player2', methods=['POST'])
def player2():
    print (request.form)
    name = request.form['name']
    choice = request.form['choice']
    player2 = Player(name, choice)
    Player.add_player_to_players(player2)
    return redirect('/play')

@app.route('/showdown')
def showdown():
    return render_template('showdown.html')