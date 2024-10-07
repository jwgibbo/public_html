#maze walking sketch

class MazeWalker:
    def __init__(self, ???):
        self.maze = ???
        self.visited_grid = ???
        self.current_step = ???
        self.start_row = ???
        self.start_col = ???

    def mark(self, row, col):
        #marks the visited grid at
        #given position with current step
        #update current step

    def find_exit(self, row, col):
        #mark current position
        self.mark(row, col)

        if self.is_exit(row, col):
            return True

        #Look up
        if self.is_valid_move(row-1, col):
            is_exit_up = self.find_exit(row-1, col)

            if is_exit_up:
                return True

        
        #Look right
        if self.is_valid_move(row, col+1):
            is_exit_right = self.find_exit(row, col+1)

            if is_exit_right:
                return True
        #Look down
        #Look left

        #if doing path to exit
        self.unmark(row, col)
        
        return False
