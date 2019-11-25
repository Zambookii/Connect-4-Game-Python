from ASCIIDisplay import ASCIIDisplay
from Board import Board
from GameController import Connect4Runner

if __name__ == "__main__":
    spacing = int(input("Please choose the board spacing: "))
    while spacing < 0:
        spacing = int(input("Invalid size, choose again: "))
    d = ASCIIDisplay(spacing)
    thegame = Connect4Runner(d)
    thegame.play_game()
