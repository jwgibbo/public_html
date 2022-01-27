#include <iostream>

//define a function that can print the 
//contents of a 2D array of ints
void printArray2D(int** arr2D, int rows, int cols)
{
	for(int i=0; i<rows; i++)
	{
		for(int j=0; j<cols; j++)
		{
			std::cout << arr2D[i][j] << '\n';
		}
	}	
}


int main()
{
	int rows = 3;
	int cols = 4;
	int** grid = nullptr;
	
	grid[rows] = new int*[row];
	
	for(int i=0; i<rows; i++)
	{
		grid[i] = new int[cols];
	}

	//fill the array with 31s
	for(int i=0; i<rows; i++)
	{
		for(int j=0; j<cols; j++)
		{
			grid[i][j] = 31;
		}
	}

	return(0);
}



