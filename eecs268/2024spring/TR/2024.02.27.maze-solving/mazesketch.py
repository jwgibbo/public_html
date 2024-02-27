#sketch of maze solving code

class MazeSolver:
    def __init__(self, ???):
        self._the_maze = ???
        self._cur_step = ???
        self._visited_grid = ???

    def find_exit(self, row, col):

        #mark current position
        self.mark(row, col)

        #Are we done?
        if self.is_exit(row, col):
            return True

        #check up
        if self.is_valid_move(row-1, col):
            is_exit_found = self.find_exit(row-1, col)
            if is_exit_found:
                return True

        #check right
        if self.is_valid_move(row, col+1):
            is_exit_found = self.find_exit(row, col+1)
            if is_exit_found:
                return True
        #check down
        #check left

        self.unmark(row, col)
        return False
        
