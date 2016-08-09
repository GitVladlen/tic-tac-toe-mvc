"""
    This is CONTROLLER
"""
from Notification import Notification

class Controller(object):
    def __init__(self, model):
        self.model = model
        pass

    def work(self):
        while self.model.isGameOver() is False:

            while True:
                try:
                    row, col = input("{player}: ".format(player=self.model.turn))
                    pass
                except Exception:
                    continue
                    pass

                if self.model.makeTurn(row, col) is True:
                    break
                    pass
                pass

            pass

        Notification.notify("onGameOver")
        pass

    def __str__(self):
        return "[controller]"
        pass
    pass
