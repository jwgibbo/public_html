import random

def lotto_num():
    return random.sample(range(1, 37), k=6)

def main():
    #define this to let the user play the lotto
    #The user has 1 billion dollars. Each time
    #they play the lotto, it costs a dollar.
    #Let the user play the lotto over and over
    #until they win or lose all their money
