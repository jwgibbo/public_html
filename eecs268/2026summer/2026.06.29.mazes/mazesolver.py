#mazesolver.py

#Sketch of a class to solve a maze

class MazeSolver:
    def __init__(self, ???):
        self._maze = ??? #2D grid of characters?
        self._visited_grid = ??? #2D grid of ints?
        self._cur_step = 0
        self._start_row = ???
        self._start_col = ???


    def solve(self, row, col):
        self._mark(row, col)

        if self._is_exit(row, col):
            return True

        #Look up
        if self._is_valid_move(row-1, col):
            is_exit_up = self.solve(row-1, col)
            if is_exit_up:
                return True

        #Look right
        if self._is_valid_move(row, col+1):
            is_exit_right = self.solve(row, col+1)
            if is_exit_right:
                return True
            
        #Look down
        #Look left

        #We are out of directions to try
        #I can unmark, if wanted
        return False


    def mark(self, row, col):
        #marks current row,col in visted grid
