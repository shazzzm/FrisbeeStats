from player import Player
class Game:
    players = []
    points = []
    our_score = 0
    their_score = 0 

    def __init__(self):
        pass

    def add_pass(self, id_player_to, id_player_from):
        pass

    def add_players(self, player_name, player_number):
        p = Player(len(players), player_name, player_number)
        players.append(p)

    def get_players(self):
        return self.players