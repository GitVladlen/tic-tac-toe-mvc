from model import Model
from view import View
from controller import Controller


def main():
    print " = Tic Tac Toe MVC Game = "
    model = Model()

    controller = Controller(model)
    view = View(model, controller)

    model.newGame()

    while model.isGameOver() is False:
        model.tick()
        pass
    pass

if __name__ == "__main__":
    main()
    pass

