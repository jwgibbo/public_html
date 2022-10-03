#Sketch of a MazeWalking class

class MazeWalker:
    def __init__(self):
        #maze contents
        #visited grid
        #current step

    def walk(row, col):
        self.mark(row, col)

        if self.is_exit(row, col):
            return True

        #if up is a valid move, try it
        if self.is_valid_move(row-1, col):
            up_works = self.walk(row-1, col)
            if up_works:
                return True

        #if right is a valid move, try it

        #if down is a valid move, try it

        #if left is a valid move, try it

        self.unmark(row, col)

        #one last thing...
