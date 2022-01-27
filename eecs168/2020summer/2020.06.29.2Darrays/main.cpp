#include <iostream>

int main()
{	
	//recall a 1D heap allocated
	int* nums = nullptr;
	int size = 5;
	
	nums = new int[size];
	
	//Goal: Make a "grid" of values
	//Solution: 2D pointer
	//Make an array of pointers!
	int** grid = nullptr;
	int numRows = 3;
	int numCols = 4;
	
	//allocate an array of pointers
	grid = new int*[numRows];
	
	//create an array of ints for
	//each int pointer
	for(int i=0; i<numRows; i++)
	{
		grid[i] = new int[numCols];
	}
	
	grid[2][3] = 55;
	
	//Nested for loops and 2D arrays
	//are great together!
	
	//Note: You need to delete[] all 
	//heap allocated arrays.
	//Be careful about order of deletion
	
	return(0);
}