#mazewalkingsketch.py

class MazeWalker:

    def __init__(self, ???):
        self._maze = ???
        self._visited_grid = ???
        self._current_step = 0
        self._start_row = ???
        self._start_col = ???

    def _find_exit(row, col):

        self._mark(row, col)
        
        if self._is_exit(row, col):
            return True

        #Look up
        if self._is_valid_move(row-1, col):
            is_exit_up = self._find_exit(row-1, col)
            if is_exit_up:
                return True

        #Look right
        if self._is_valid_move(row, col+1):
            is_exit_right = self._find_exit(row, col+1)
            if is_exit_right:
                return True

        #Look down
        if self._is_valid_move(row+1, col):
            is_exit_down = self._find_exit(row+1, col)
            if is_exit_down:
                return True

        #Look left

        #if we run out of options unmark and back up
        self._unmark(row, col)
        return False
        
