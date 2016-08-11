"""
    This is VIEW
"""


class View(object):
    def __init__(self, model, controller):
        self.model = model
        self.controller = controller

        self.symbols = {
            self.model.EMPTY: "#",
            self.model.PLAYER1: "X",
            self.model.PLAYER2: "O"
            }

        self.model.EventMakeTurn.addObserver(self._onMakeTurn)
        self.model.EventGameOver.addObserver(self._onGameOver)
        pass

    def __printGrid(self):
        grid = self.model.getGrid()

        print "+ 0 1 2 +"
        for row_index, row in enumerate(grid):
            print row_index,
            for cell in row:
                print self.symbols[cell],
                pass
            print "|"
            pass
        print "+ - - - +"

        pass

    def __printPrompt(self):
        print "Player {player_symbol} turn <row, column>: ".format(
            player_symbol=self.symbols[self.model.turn])
        pass

    def _onMakeTurn(self):
        self.__printGrid()
        self.__printPrompt()

        while True:
            try:
                row, col = input()
                pass
            except Exception:
                continue
                pass

            if row not in range(3):
                continue
                pass

            if col not in range(3):
                continue
                pass

            self.controller.turn(row, col)
            break
            pass

        pass

    def _onGameOver(self):
        self.__printGrid()

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
