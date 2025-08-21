#mazewalker.py

#Purpose: Sketch of what a maze
#walking class might look like

class MazeWalker:
    def __init__(???):
        self.maze = ???
        self.visted_grid = ???
        self.current_step = ???
        self.start_row = ???
        self.start_col = ???

    def step(self, row, col):
        self.mark(row, col) #helper method

        if self.is_exit(row, col):
            return True

        #Order to look for moves: U, R, D, L

        #Up
        if self.is_valid_move(row-1, col):
            #does going up lead to an exit?
            is_exit_up = self.step(row-1, col)

            if is_exit_up:
                return True
        #Right
        if self.is_valid_move(row, col+1):
            #does going right lead to an exit?
            is_exit_right = self.step(row, col+1)

            if is_exit_right:
                return True

        #Down
        if self.is_valid_move(row+1, col):
            #does going down lead to an exit?
            is_exit_down = self.step(row+1, col)

            if is_exit_down:
                return True

        #Left
        #Plays out pretty much the same as others

        
        #If we tried all the direct and haven't
        #returned yet, what does that mean?
        #We're at a deadend!

        #unmark, if you're doing path to exit
        return False 
        
        
