'''The controller in the design'''

from Board import Board
from Player import Player
from Piece import *
from ASCIIDisplay import *

class Connect4Runner:
    def __init__(self, display):
        self.displayDriver = display
        self.board = Board()

    def reinitialize(self, display):
        self.displayDriver = display
        self.board = Board()

    def play_game(self):
        '''Starts the actual game. Defaults to 2 players.'''
        totalPieces = self.board.rows * self.board.cols
        player1 = Player(1, 'R', "Jesse")
        player2 = Player(2, 'B', "Daniel")
        print("Type the column in which you wish to move.")
        turn_count = 0
        while True:
            turn_count += 1
            if(turn_count % 2 == 1):
                current_player = player1
            else:
                current_player = player2

            self.displayDriver.printState(self.board)
            move = ASCIIDisplay.prompt_for_move(turn_count, current_player.playerNumber, current_player.pieceMarker)-1
            while move < 0 or move > self.board.cols-1:
                ASCIIDisplay.invalid_move_out_of_bounds(move+1)
                move = ASCIIDisplay.prompt_for_move(turn_count, current_player.playerNumber, current_player.pieceMarker)-1

            while self.board.check_if_full(move) == True:
                ASCIIDisplay.col_full_error(move+1)
                move = ASCIIDisplay.prompt_for_move(turn_count, current_player.playerNumber, current_player.pieceMarker)-1
                while move < 0 or move > self.board.cols-1:
                    ASCIIDisplay.invalid_move_out_of_bounds(move+1)
                    move = ASCIIDisplay.prompt_for_move(turn_count, current_player.playerNumber, current_player.pieceMarker)-1

            aPiece = Connect4Piece(current_player, self.board, move)
            self.board.add_piece(aPiece)
            totalPieces -= 1

            if totalPieces == 0:
                print("Tie Game!")
                break

            if self.check_if_winner(aPiece, current_player) == True:
                self.displayDriver.printState(self.board)
                if ASCIIDisplay.isWinner(current_player) == 'y':
                    restartGame()
                    break
                else:
                    break

    def check_if_winner(self, piece, player):
        check = self.board.check_if_winner(piece, player)
        return check


def restartGame():
    spacing = int(input("Please choose the board spacing: "))
    d = ASCIIDisplay(spacing)
    thegame = Connect4Runner(d)
    thegame.play_game()
