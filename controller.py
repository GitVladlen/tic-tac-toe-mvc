"""
    This is CONTROLLER
"""


class Controller(object):
    def __init__(self, model):
        self.model = model
        pass

    def turn(self, row, col):
        self.model.makeTurn(row, col)
        pass

    def __str__(self):
        return "[controller]"
        pass
    pass
