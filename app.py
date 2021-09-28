import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

board = gameboard.GameBoard()

while True:
    board.printBoard(board.player.rowPosition, board.player.columnPosition)
    selection = input("Make a move: ")
    board.player_movement(selection)

    if board.checkWin(board.player.rowPosition, board.player.columnPosition):
        print("You win")
        quit()

