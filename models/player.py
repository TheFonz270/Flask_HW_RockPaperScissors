players = []

class Player():
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice


    def add_player_to_players(player):
        if player in players:
            for n in players:
                if n == player:
                    players.remove(n) 
                    players.append(player)
        else:
            players.append(player)
