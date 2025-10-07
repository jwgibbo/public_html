#mazewalker.py

class MazeWalker:
    def __init__(self, ???):
        self._the_maze = ???
        self._visited_grid = ???
        self._step_counter = 0


    def walk_maze(self, row, col):
        #mark current position
        self._mark(row, col)

        if self._is_exit(row, col):
            return True

        #look UP, see if it's valid
        if self._is_valid_move(row-1, col):
            is_exit_found = self.walk_maze(row-1, col)
            if is_exit_found:
                return True
        #look RIGHT, see if it's valid
        if self._is_valid_move(row, col+1):
            is_exit_found = self.walk_maze(row, col+1)
            if is_exit_found:
                return True

        #board work: finish writing the walk_maze method
        #               check down, check left, ???, ???
        #            Feel free to call more helper methods



    def _mark(self, row, col):
        #marks the position in vistited grid
        pass

        
