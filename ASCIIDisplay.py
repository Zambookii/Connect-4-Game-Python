'''The view of the design'''

class ASCIIDisplay:
    def __init__(self,spacing = 1):
        self.spacing = spacing-1

    def printState(self, b):
        fullString = ""
        across = range(0,b.cols)
        #up = range(0, b.rows, 1)
        up = range(b.rows-1,-1,-1)
        spaces = range(self.spacing)
        for i in up:
            top = "+"
            for j in across:
                for k in spaces:
                    top = top + "-"
                top = top + "-"
                for k in spaces:
                    top = top + "-"
                top = top + "+"
            top = top + "\n"
            fullString = fullString + top
            top = "+"
            for j in across:
                for k in spaces:
                    top = top + " "
                top = top + str(b.cells[j][i]) #.piece.disp
                for k in spaces:
                    top = top + " "
                if(j == b.cols):
                    top = top + "+"
                else:
                    top = top + "|"
            top = top + "\n"
            fullString = fullString + top
        top = "+"
        #bottom
        for j in across:
            for k in spaces:
                top = top + "-"
            top = top + "-"
            for k in spaces:
                top = top + "-"
            top = top + "+"
        top = top + "\n"
        fullString = fullString+top
        #indices
        top = " "
        for j in across:
            for k in spaces:
                top = top + " "
            top = top + str(j+1)
            for k in range(self.spacing-len(str(j+1))+1):
                top = top + " "
            top = top + " "
        top = top + "\n"
        fullString = fullString+top
        print(fullString)

    @staticmethod
    def prompt_for_move(turn_count, playerNumber, player_symbol):
        print("Turn {}: Player {} ({}), choose your move: ".format(turn_count, playerNumber, player_symbol), end='')
        move = int(input())
        return move

    @staticmethod
    def invalid_move_out_of_bounds(loc):
        print("Invalid move, {} is outside board, try again: ".format(loc))

    @staticmethod
    def col_full_error(loc):
        print("Invalid move, column {} is full, try again: ".format(loc))

    @staticmethod
    def isWinner(player):
        print("Player {} Wins! Play again? (y/n): ".format(player.playerNumber, player.playerName), end='')
        playagain = input()
        if playagain == "y":
            return playagain
        else:
            print("Goodbye!")
