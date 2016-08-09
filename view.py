"""
    This is VIEW
"""
from Notification import Notification

class View(object):
    def __init__(self, model):
        self.model = model

        Notification.addObserver(self, "onMakeTurn")
        Notification.addObserver(self, "onGameOver")

        self.update()
        pass

    def onEvent(self, event):
        if event == "onMakeTurn":
            self.update()
            pass
        if event == "onGameOver":
            self.onGameOver()
            pass
        pass

    def update(self):
        grid = self.model.getGrid()

        print "+ 0 1 2 +"
        for row_index, row in enumerate(grid):
            print row_index,
            for cell in row:
                if cell == self.model.EMPTY:
                    print "#",
                    pass
                elif cell == self.model.PLAYER1:
                    print "X",
                    pass
                elif cell == self.model.PLAYER2:
                    print "O",
                    pass
                pass
            print "|"
            pass
        print "+ - - - +"
        pass

    def onGameOver(self):
        if self.model.isPlayer1Win() is True:
            print " = Player 1 Win ="
            pass
        elif self.model.isPlayer2Win() is True:
            print " = Player 2 Win ="
            pass
        elif self.model.isDraw() is True:
            print " = Draw ="
            pass
        pass

    def __str__(self):
        return "[view]"
        pass
    pass
