class Game():
    def __init__(self, players):
        self.players = players
        self.game_logic = {"Rock":{"Rock":"Tie", "Paper":1, "Scissors":0}, "Paper":{"Rock":0, "Paper":"Tie", "Scissors":1}, "Scissors":{"Rock":1, "Paper":0, "Scissors":"Tie"}}
    

    
    def play_game(self, players):
        winner = self.game_logic[players[0].choice][players[1].choice]
        if winner == 1:
            loser = 0 
        elif winner == 0:
            loser = 1
        return winner