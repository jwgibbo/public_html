

//sketch of walk


//public facing walk
bool MazeWalker::walk()
{
	return( walk(m_startRow, m_startCol) );	
}


bool MazeWalker::walk(int row, int col)
{
	//mark current position
	mark(row, col);
	
	//base cases?
	//1) how will we know when we're at a deadend?
	//2) if we're on the exit, return true
	if( isExit(row, col) )
	{
		return( true );
	}
	
	//look around for valid in the 
	//order: up, right, down, left
	
	//if I can move up
		//move up and see if it leads to a solution
		//if so, return true
	
	//if I can move right
		//move right and see if it leads to a solution
		//if so, return true
		
	//repeat for remaining possible moves
	
	
	//What do I know if I didn't find a solution?
	//I know this position is NOT on a path 
	//to a solution
	
	//unmark this position
	//return false
}