#include <iostream>

//Goal: Write a function that sets
// 		every index in a 2D of ints
//		to -1
void init2D(int* arr2D[], int rows, int cols)
{
	//Draw the call stack and heap
	for(int i=0; i<rows; i++)
	{
			for(int j=0; j<cols; j++)
			{
				arr2D[i][j] = -1;
			}
	}
}

//Goal: Write a function that prints
//		a 2D array of ints.
//		Each row on it's own line
void print2D(int** arr2D, int rows, int cols)
{
	for(int i=0; i<rows; i++)
	{
		for(int j=0; j<cols; j++)
		{
			std::cout << arr2D[i][j] << ' ';
		}
		std::cout << '\n';
	}
}

int main()
{
	int** grid = nullptr;
	int rows = 3;
	int cols = 4;
	
	grid = new int*[rows];
	
	for(int i=0; i<rows; i++)
	{
		grid[i] = new int[cols];
	}
	
	init2D(grid, rows, cols);
	print2D(grid, rows, cols);
	
	//don't forget to delete!
	return(0);
}
