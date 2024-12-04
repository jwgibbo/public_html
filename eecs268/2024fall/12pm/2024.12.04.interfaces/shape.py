#shape.py

class Shape:
    #No __init__ because we won't
    #make instances of Shape

    def area(self):
        raise NotImplementedError('area not defined by subclass')
