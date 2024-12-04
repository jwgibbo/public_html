#shape.py
class Shape:
    #No __init__ because we won't
    #ever make an instance of the Shape class

    def area(self):
        raise NotImplementedError('subclass did not define area')
