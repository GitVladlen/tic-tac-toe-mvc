class NotificationClass(object):
    observers = {}

    def addObserver(self, observer, event):
        if event not in self.observers:
            self.observers[event] = [observer,]
            pass
        else:
            self.observers[event].append(observer)
            pass
        pass

    def removeObserver(self, observer, event):
        if event not in self.observers:
            return
            pass

        if observer not in self.observers[event]:
            return
            pass

        self.observers[event].remove(observer)
        pass

    def notify(self, event):
        if event not in self.observers:
            return
            pass

        for observer in self.observers[event]:
            observer.onEvent(event)
            pass
        pass
    pass

# global object
Notification = NotificationClass()
