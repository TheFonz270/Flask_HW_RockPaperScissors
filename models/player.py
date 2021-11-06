players = []
choice1 = "Rock"
choice2 = "Rock"

class Player():
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice


    def add_player_to_players(player):
        if len(players) < 2:
            players.append(player)
        else:
            players.remove(players[0])
            players.append(player)
