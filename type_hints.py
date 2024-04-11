var: int = 1


class Duck:
    def __init__(self): ...

    def __getattr__(self, attr):
        if attr == "quack":
            return lambda: print("quack")
        elif attr == "swim":
            return lambda: print("splash")
        else:
            raise AttributeError


duck = Duck()
duck.quack()
duck.swim()
duck.fly()
duck.eat()

var: int = 1
var = "hi"
