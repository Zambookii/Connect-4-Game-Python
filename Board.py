'''The model in the design'''

from Cell import Cell
from Piece import Piece


class Board:
    '''A container for the collection of spaces in the playing field'''
    def __init__(self, col=7, row=6):
        '''Tic Tac Toe defaults to a 3 by 3 board

        cells is a 2 dimensional list of cell objects
        The first list is the list of columns
        Each column contains a list of rows
        How you construct your board is up to you, just be consistent'''
        self.rows = row
        self.cols = col
        self.cells = []
        for cell_col in range(self.cols):
            new_row = []
            for cell_row in range(self.rows):
                new_row.append(Cell(cell_col, cell_row))
            self.cells.append(new_row)

    def add_piece(self, p):
        '''Adds a piece onto the board'''
        self.cells[p.col][p.row].piece = p
        self.cells[p.col][p.row].occupied = True

    def checkBounds(self, col, row):
        '''Used to check if the bounds are correct'''
        if col < 0 or col > self.cols-1:
            return False
        elif row < 0 or row > self.rows-1:
            return False
        elif self.cells[col][row].occupied == False:
            return False
        else:
            return True

    def check_if_winner(self, piece, player):
        '''Checks all possible combinations of winning'''
        piece_col = piece.col
        piece_row = piece.row
        player_symbol = piece.disp

        if self.checkDirection(piece_col, piece_row, 0, -1, player_symbol) == 4:
            return True

        if self.checkDirection(piece_col, piece_row, -1, -1, player_symbol) == 4:
            return True

        if self.checkDirection(piece_col, piece_row, 1, -1, player_symbol) == 4:
            return True

        if self.checkDirection(piece_col, piece_row, -1, 0, player_symbol) == 4:
            return True

        if self.checkDirection(piece_col, piece_row, 1, 0, player_symbol) == 4:
            return True


    def checkDirection(self, piece_col, piece_row, piece_col_add, piece_row_add, player_symbol):
        '''Function used to check if 4 pieces are connected'''
        connected_pieces = 1 #need 4 to win
        test_col = piece_col + piece_col_add
        test_row = piece_row + piece_row_add
        if self.checkBounds(test_col, test_row) == True:
            while self.cells[test_col][test_row].piece.disp == player_symbol:
                connected_pieces += 1
                if connected_pieces == 4:
                    return connected_pieces
                test_col += piece_col_add
                test_row += piece_row_add
                if(self.checkBounds(test_col, test_row) == False):
                    break

    def getRow(self, col):
        '''Checks the next available row that the piece can be put'''
        for row in range(0, self.rows):
            if(self.cells[col][row].occupied == False):
                return row

    def check_if_full(self, col):
        '''Checks if the column is full or not, if it is true return true, else false'''
        if(self.cells[col][self.rows-1].occupied == True):
            return True
        else:
            return False
