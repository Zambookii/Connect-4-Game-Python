
class Player:
    def __init__(self, player_number=-1, piece_marker="?", player_name="Unknown", _pieces=-1):
        '''Player gets a number, piece marker, name, and amount of pieces'''
        self.playerNumber = player_number
        self.pieceMarker = piece_marker
        self.playerName = player_name
        self.pieces = _pieces;
