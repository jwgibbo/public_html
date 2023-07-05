#sketch of the MazeWalker class

class MazeWalker:
    def __init__(self, ???):
        #create your maze, visited grid
        #and store your start row/col

        #OR, maybe you have Maze class that
        #just handle storing maze contents
        #and helper methods like get_pos(row, col)

    def step(self, row, col):
        #mark current position
        self.mark(row, col)

        #Check if we found exit
        if self.is_exit(row, col):
            return True

        #Check up for a valid step
        if self.is_valid_step(row-1, col):
            leads_to_exit = self.step(row-1, col)
            if leads_to_exit:
                return True

        #Check right for a valid step
        if self.is_valid_step(row, col+1):
            leads_to_exit = self.step(row, col+1)
            if leads_to_exit:
                return True

        #Check down

        
        #Check left

        #???

        #???
        
