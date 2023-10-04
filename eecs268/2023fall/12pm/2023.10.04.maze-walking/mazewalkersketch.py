#mazewalkersketch.py


class MazeWalker:
    def __init__(self, ???):
        self._the_maze = ???
        self._visited_grid = ???
        self._current_step = 0
        self._start_row = ???
        self._start_col = ???
        
    def _mark(self, row, col):
        self._visited_grid[row][col] = self._current_step
    

    def _find_exit(row, col):
        self._current_step += 1
        self._mark(row, col)

        if self._is_exit(row, col):
            return True

        #Look up 
        if self._is_valid_move(row-1, col):
            #See if up leads to an exit
            is_exit_up = self._find_exit(row-1, col)

            if is_exit_up:
                return True

        #Look right
        if self._is_valid_move(row, col+1):
            #See if right leads to an exit
            is_exit_right = self._find_exit(row, col+1)

            if is_exit_right:
                return True

        #Look Down
            #same sort of stuff as other directions

        #Look Left
            #same sort of stuff as other
        self._unmark(row, col)    
        return False
