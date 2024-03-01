#A sketch of a maze solving class

class MazeSolver:
    def __init__(self, ???):
        self._the_maze = ???
        self._visited_grid = ???
        self._current_step = ???

    def find_exit(self, row, col):
        self.mark(row, col)


        if self.is_exit(row, col):
            return True

        #check for possible moves

        #check up
        if self.is_valid_move(row-1, col):
            #let's move there!
            is_exit_found = self.find_exit(row-1, col)
            if is_exit_found:
                return True
            else???
        
