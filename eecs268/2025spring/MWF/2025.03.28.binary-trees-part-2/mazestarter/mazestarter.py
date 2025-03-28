#mazerstarter.py


class MazeSolver:
    def __init__(self, ???):
        self.the_maze = ???
        self.visited_grid = ???
        self.current_step = ???


    def solve(self, row, col):
        self.mark(row, col)
        
        if self.is_exit(row, col):
            return True

        #look Up
        if self.is_valid_move(row-1, col):
            is_exit_up = self.solve(row-1, col)
            if is_exit_up:
                return True

        #look Right
        if self.is_valid_move(row, col+1):
            is_exit_right = self.solve(row, col+1)
            if is_exit_right:
                return True

        #Repeat the same actions for DOWN & LEFT

        #If none of the directions led to an exit
        #we on a path to a dead end and we need
        #to backtrack

        #here is where you would unmark
        return False
