#Sketch of a Maze Walking class

class MazeWalker:
    def __init__(self, ???):
        self.maze = _______
        self.visited_grid =_______
        self.start_row = _____
        self.start_col = _____
        self.current_step = ______

    def mark(self, row, col):
        #handles the marking of the
        #the visited grid and update the
        #current step

    def find_exit(self, row, col):
        #Mark the current position
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

        #If you only want path to exit
        self.unmark(row, col)

        return False
