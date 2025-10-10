#mazewalker.py


class MazeWalker:
    def __init__(self, ???):
        self._maze = ???
        self._start_row = ???
        self._start_col = ???
        self._visited_grid = ???
        self._step_counter = 0

    def walk(self, row, col):
        self._mark(row, col)
        
        if self._is_exit(row, col):
            return True

        #Look for a valid move in the
        #order Up, Right, Down, Left

        #Up
        if self._is_valid_move(row-1, col):
            is_exit_found = self.walk(row-1, col)
            if is_exit_found:
                return True

        #Right
        if self._is_valid_move(row, col+1):
            is_exit_found = self.walk(row, col+1)
            if is_exit_found:
                return True
        #Down
        #Left
            
        #If we haven't found an exit,
        #out of options to try
        #Need to backtrack
        self._unmark(row, col)
        return False
    
    def _is_exit(self, row, col):
        #returns True if row,col is exit
        #returns False otherwise
