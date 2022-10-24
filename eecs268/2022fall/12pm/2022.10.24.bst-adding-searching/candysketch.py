#candysketch.py

#Sketch of Candy class

class Candy:
    def __init__(self, name):
        self.name = name
        self.rating = ???
        self.ingredients = []

    #magic methods to overload
    def __lt__(self, other):
        #if other is a Candy then
        #compare their names
        #if other is a string then
        #compare self.name to string


    def __eq__(self, other):

    def __gt__(self, other):
