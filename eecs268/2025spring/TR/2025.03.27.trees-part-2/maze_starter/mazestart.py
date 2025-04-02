#mazestarter.py

class MazeWalker:
    def __init__(self, ???):
        self.the_maze = ???
        self.visited_grid = ???
        self.cur_step = 0
        #where do get start position?

    def solve(self, row, col):
        self.mark(row, col)
    
        if self.is_exit(row, col):
            return True

        #look UP for a valid move
        if self.is_valid_move(row-1, col):
            is_exit_up = self.solve(row-1, col)
            if is_exit_up:
                return True

        #look RIGHT
        if self.is_valid_move(row, col+1):
            is_exit_right = self.solve(row, col+1)
            if is_exit_right:
                return True

        #look DOWN
        if self.is_valid_move(row+1, col):
            is_exit_down = self.solve(row+1, col)
            if is_exit_down:
                return True

        #look LEFT
        #same as other steps, just tweak coordinate

        #here you would unmark

        #Exit wasn't found. We're on the way to dead end
        return False
            
