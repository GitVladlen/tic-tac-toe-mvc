from Functor import *


class Event(object):
    __slots__ = "name", "observers"

    def __init__(self, name):
        self.name = name
        self.observers = []
        pass

    def addObserver(self, fn, *args, **kwargs):
        observer = FunctorStore(fn, args, kwargs)

        if observer in self.observers:
            return None
            pass

        self.observers.append(observer)

        return observer
        pass

    def removeObserver(self, observer):
        if observer not in self.observers:
            return
            pass

        self.observers.remove(observer)
        pass

    def removeObservers(self):
        self.observers = []
        pass

    def __call__(self, *args, **kwargs):
        for observer in self.observers[:]:
            if observer not in self.observers:
                continue
                pass

            observer(*args, **kwargs)
            pass
        pass

    pass
