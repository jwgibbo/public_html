#ifndef MAZE_WALKER_H
#define MAZE_WALKER_H

#include <string>
#include <fstream>

//Sketch of a MazeWalker class
//NOT a complete definition
class MazeWalker
{
	//What will the outside world need to call?
	public:
	//Initialize the visited array
	MazeWalker(std::string mazeFileName);
	
	//returns true only if it found to the exit
	bool walk();
	
	//prints solution to terminal
	void printSolution();
	
	//What will our class use/maintain internally?
	private:
	int m_numRows;
	int m_numCols;
	char** m_maze;
	int** m_visited;
	int m_startRow;
	int m_startCol;
	
	
	//return true if it's a legal move
	//return false otherwise (off the array,
	//position is a wall, position is visited/marked)
	bool isValidMove(int row, int col);
	bool isMarked(int row, int col);
	bool isWall(int row, int col);
	bool isOffArray(int row, int col);
	
	bool isExit(int row, int col);
	
	void mark(int row, int col);
	void unmark(int row, int col);
	
	//recursive walking method used by 
	//public walk
	bool walk(int row, int col);
};

#endif