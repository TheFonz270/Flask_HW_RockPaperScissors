from app import app
from flask import render_template, redirect, request
from models.player import Player, players
from models.game import Game
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
    name1 = str(request.form['name'])
    choice1 = str(request.form['choice'])
    player1 = Player(name1, choice1)
    Player.add_player_to_players(player1)
    return redirect('/play')

@app.route('/player2', methods=['POST'])
def player2():
    print (request.form)
    name2 = str(request.form['name'])
    choice2 = str(request.form['choice'])
    player2 = Player(name2, choice2)
    Player.add_player_to_players(player2)
    return redirect('/play')

@app.route('/showdown')
def showdown():
    return render_template('showdown.html')

# @app.route('/<choice1>/<choice2>')
@app.route('/Rock/Rock')
@app.route('/Rock/Paper')
@app.route('/Rock/Scissors')
@app.route('/Paper/Rock')
@app.route('/Paper/Paper')
@app.route('/Paper/Scissors')
@app.route('/Scissors/Rock')
@app.route('/Scissors/Paper')
@app.route('/Scissors/Scissors')
def play_game():    
    game = Game(players)
    result = game.play_game(players)
    if result == 1:
        loser = 0
    elif result == 0:
        loser = 1
    else:
        loser = "none"
    return render_template('result.html', result=result, players=players, loser=loser)