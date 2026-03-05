#mazesolver.py

class MazeSolver:
    def __init__(self, ???):
        self._maze = ???
        self._visited_grid = ???
        self._start_row = ???
        self._start_col = ???
        self._current_step


    def solve(self, row, col):
        self._mark(row, col)
    
        if self._is_exit(row, col):
            return True

        #UP
        if self._is_valid_move(row-1, col):
            is_exit_up = self.solve(row-1, col)

            if is_exit_up:
                return True
        #RIGHT
        if self._is_valid_move(row, col+1):
            is_exit_right = self.solve(row, col+1)

            if is_exit_right:
                return True

        #DOWN

        #LEFT

        #This position is NOT going to lead to
        #an exit; Failure case
        self._unmark(row, col)
        return False
