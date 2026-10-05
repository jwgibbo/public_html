#mazesolver.py

class MazeSolver:
    def __init__(self, ???):
        self.maze = ???
        self.visted_grid = ???
        self.start_row = ???
        self.start_col = ???
        self.step_count = 0

    def rec_walk(self, row, col):
        self.mark(row, col)    
        
        if self.is_exit(row, col):
            return True

        #look Up
        if self.is_valid_move(row-1, col):
            is_exit_up = self.rec_walk(row-1, col)
            if is_exit_up:
                return True

        #look right
        if self.is_valid_move(row, col+1):
            is_exit_right = self.rec_walk(row, col+1)
            if is_exit_right:
                return True

        #look down

        #look left

        #Know I'm stuck (e.g. dead-end)
        #If you're unmark, do that now
        #return failure value
        
            



    def is_exit(self, row, col):
        #define this to check the row
        #and col for the 'E'
