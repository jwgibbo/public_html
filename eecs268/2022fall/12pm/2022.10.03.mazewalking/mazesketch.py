#Sketch of the MazeWalking class

class MazeWalker:
    def __init__(self, maze_file):
        #the maze contents
        #the visited grid
        #current step
        

    def walk(row, col):
        self.mark(row, col)

        if self.is_exit(row, col):
            return True

        #If up is a valid move try it
        if self.is_valid_move(row-1, col):
            up_worked = self.walk(row-1, col)
            if up_worked:
                return True

        #If right is a valid move try it
            
        #If down is a valid move try it

        #If left is a valid move try it

        #Unmark (assume a helper method)

        #One last thing...
        
        
