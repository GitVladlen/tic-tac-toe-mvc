"""
    This is MODEL
"""
from Notification import Notification

class Model(object):
    EMPTY = 0
    PLAYER1 = 1
    PLAYER2 = 2

    def __init__(self):
        super(Model, self).__init__()
        self.grid = None
        self.turn = self.PLAYER1

        self.initGrid()
        pass

    def initGrid(self):
        self.grid = [[self.EMPTY for x in range(3)] for x in range(3)]
        pass

    def changePlayer(self):
        if self.turn == self.PLAYER1:
            self.turn = self.PLAYER2
            pass
        else:
            self.turn = self.PLAYER1
            pass
        pass

    def makeTurn(self, row, col):
        if row not in range(3):
            return False
            pass

        if col not in range(3):
            return False
            pass

        if self.grid[row][col] != self.EMPTY:
            return False
            pass

        self.grid[row][col] = self.turn
        self.changePlayer()

        Notification.notify("onMakeTurn")
        return True
        pass

    def getGrid(self):
        return self.grid
        pass

    def isGameOver(self):
        if self.isPlayer1Win() is True:
            return True

        if self.isPlayer2Win() is True:
            return True

        if self.isDraw() is True:
            return True

        return False
        pass

    def checkWin(self, player):
        blocks = (
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),

            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2)),

            ((0, 0), (1, 1), (2, 2)),
            ((0, 2), (1, 1), (2, 0)),
        )

        for block in blocks:
            win = True
            for coordinates in block:
                row, col = coordinates
                if self.grid[row][col] != player:
                    win = False
                    break
                    pass
                pass

            if win is True:
                return True
                pass
            pass

        return False
        pass

    def isPlayer1Win(self):
        if self.checkWin(self.PLAYER1) is True:
            return True
            pass

        return False
        pass

    def isPlayer2Win(self):
        if self.checkWin(self.PLAYER2) is True:
            return True
            pass

        return False
        pass

    def haveEmptyCells(self):
        for row in self.grid:
            for cell in row:
                if cell == self.EMPTY:
                    return True
                    pass
                pass
            pass

        return False
        pass

    def isDraw(self):
        if self.haveEmptyCells() is True:
            return False
            pass

        if self.isPlayer1Win() is True:
            return False
            pass

        if self.isPlayer2Win() is True:
            return False
            pass

        return True
        pass

    def __str__(self):
        return "[model]" + str(self.grid)
        pass
    pass
