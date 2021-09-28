import player


class GameBoard:
    def __init__(self):
        self.winningRow = 0
        self.winningColumn = 2
        self.player = player.Player(3,2)
        self.board = [
            [" * ", " * ", "   ", " * ", " * ", " * ", " * ", " * "],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * ",
                " * "
            ],
            [
                " * ",
                "   ",
                " * ",
                " * ",
                "   ",
                " * ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                " * ",
                "   ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                " * ",
                " * ",
                " * ",
                " * ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "  ",
                " * ",
                "   ",
                " * "
            ],
            [" * ", " * ", " * ", " * ", " * ", " * ", " * ", " * "],
        ]

    def printBoard(self, playerRow, playerColumn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == playerRow and j == playerColumn:
                    print("P", end="")
                else:
                    print(self.board[i][j], end="")
            print("")

    def checkMove(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("*") != -1:
            print("Can't move there!")
            return False
        return True

    def player_movement(self, selection):
        if(selection == "w"):
            if self.checkMove(self.player.rowPosition - 1, self.player.columnPosition):
                self.player.moveUp()
        elif(selection == "s"):
            if self.checkMove(self.player.rowPosition + 1, self.player.columnPosition):
                self.player.moveDown()
        elif(selection == "a"):
            if self.checkMove(self.player.rowPosition, self.player.columnPosition - 1):
                self.player.moveLeft()
        elif(selection == "d"):
            if self.checkMove(self.player.rowPosition, self.player.columnPosition + 1):
                self.player.moveRight()
        else:
            print("Invalid entry! Please try again")

    def checkWin(self, playerRow, playerColumn):
        return playerRow == self.winningRow and playerColumn == self.winningColumn


