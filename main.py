from model import Model
from view import View
from controller import Controller

def main():
    print " Start for Tic Tac Toe MVC Game!!!"
    model = Model()
    view = View(model)
    controller = Controller(model)

    controller.work()
    pass

if __name__ == "__main__":
    main()
    pass

