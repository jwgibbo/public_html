#candycketch.py

class Candy:
    def __init__(self, name, candy_id):
        self.name = name
        self.candy_id = candy_id
        self.rating = 0
        self.ingredients = []

    #The overloading of <, >, ==

    def __lt__(self, other):
        #if other is a Candy,
        #compare their candy_ids
        #if other is an int, compare
        #self.candy_id to that int
        #You can use isinstance(other, type)
        #to learn what other is

    def __gt__(self, other):

    def __eq__(self, other):
        
        
