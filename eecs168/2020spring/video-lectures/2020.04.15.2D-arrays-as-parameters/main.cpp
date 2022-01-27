#include <iostream>


void fill2DArray(int** arr2D, int rows, int cols)
{
	int num = 0;
	
	for(int i=0; i<rows; i++)
	{
		for(int j=0; j<cols; j++)
		{
			arr2D[i][j] = num;
			num++;
		}
	}
}

void print2DArray(int* arr2D[], int rows, int cols)
{
	for(int i=0; i<rows; i++)
	{
		for(int j=0; j<cols; j++)
		{
			std::cout << arr2D[i][j] << ' ' ;
		}
		std::cout << '\n';
	}
}

int main()
{
	int** grid = nullptr;
	
	//grid is int**
	grid = new int*[3];
	
	for(int i=0; i<3; i++)
	{
		//grid[i] is an int*
		grid[i] = new int[4];
	}
	
	fill2DArray(grid, 3, 4);
	print2DArray(grid, 3, 4);
	return(0);
}


/*BOARD WORK
1) Create function that takes a 2D array of ints and returns
	the largest value in the array.
	
2) Create a function that takes a 2D array of ints and a target column to print. e.g. if the caller passes 2 as the 
target column, then print the 3rd column (see video).
The goal is to print a desired column. 
*/
