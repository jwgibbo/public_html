#mazewalker.py


class MazeWalker:
    def __init___(self, ???):
        #initialize member variables

    def walk_to_end(self, row, col):
        #Step 1: Mark current position
        self.mark(row, col)

        #Step 2: Check for exit
        if self.is_exit(row, col):
            return True

        #Step 3: Looking for valid moves

        #Look up
        if self.is_valid_move(row-1, col):
            up_leads_to_exit = self.walk_to_end(row-1, col)
            if up_leads_to_exit:
                return True
        #Look right
        if self.is_valid_move(row, col+1):
            right_leads_to_exit = self.walk_to_end(row, col+1)
            if right_leads_to_exit:
                return True
        #Board work, finish the definition
        #Look down
        #Look left

        #If we make it passed all the checks, we're on a path or at
        #a dead end

        #What do we do? Feel free to make up more methods
            


    def mark(self, row, col):
        #mark the current position
        #in the visited grid with
        #current step
