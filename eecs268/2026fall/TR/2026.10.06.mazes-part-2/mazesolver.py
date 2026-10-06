#mazesolver.py

class MazeSolver:
    def __init__(self, ???):
        self.maze = ???
        self.visited_grid = ???
        self.start_row = ???
        self.start_col = ???
        self.step_count = ???

    def rec_walk(self, row, col):
        self.mark(row, col)

        if self.is_exit(row, col):
            #hand back success value
            return True

        #look up
        if self.is_valid_move(row-1, col):
            is_exit_up = self.rec_walk(row-1,col)
            if is_exit_up:
                return True

        #look right
        if self.is_valid_move(row, col+1):
            is_exit_right = self.rec_walk(row, col+1)
            if is_exit_right:
                return True

        #look down

        #look left

        #If we make to this line we're stuck
        #If we're doing path to exit, unmark
        #return a failure value


    def mark(self, row, col):
        #marks the visited grid
        #at (row, col)
