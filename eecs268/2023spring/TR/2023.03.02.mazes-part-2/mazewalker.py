#mazewalker.py


class MazeWalker:
    def ___init___(self, ???):
        #Create all needed members
        #e.g. visited_grid

    def solve_maze(self, row, col):
        #Step 1: Mark current position
        self.mark(row, col)

        #Step 2: Check for exit
        if self.is_exit(row, col):
            return True

        #Step 3-6: Check directions

        #Check up
        if self.is_valid_move(row-1, col):
            #Does moving up lead to an exit?
            is_exit_found = self.solve_maze(row-1, col)

            if is_exit_found:
                return True

        #Check right
        if self.is_valid_move(row, col+1):
            #Does moving right lead to an exit?
            is_exit_found = self.solve_maze(row, col+1)

            if is_exit_found:
                return True
        #Board work: finish our solve_maze definition
        #Check down

        #Check left

        #You're on the path to a dead end
        #Feel free to make up more methods
        ????
        
        
