class Cell:
    def __init__(self, col = -1, row = -1):
        self.row = row
        self.col = col
        self.piece = None #null
        self.occupied = False

    def empty(self):
        return not self.occupied

    def owned_by(self, player):
        return False

    def __str__(self):
        if self.occupied:
            return str(self.piece)
        return " "
