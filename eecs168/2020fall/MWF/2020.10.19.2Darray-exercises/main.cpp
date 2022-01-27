#include <iostream>

int main()
{
	//RECAP:
	//Create a 2D array of chars
	//3 rows 4 columns
	//Fill it with '?'
	char** grid = nullptr;
	int rows = 3;
	int cols = 4;
	
	grid = new char*[rows];
	
	grid = new char*[rows+10];
	
	for(int i=0; i<rows; i++)
	{
		grid[i] = new char[cols];		
	}
	
	for(int i=0; i<rows; i++)
	{
		for(int j=0; j<cols; j++)
		{
			grid[i][j] = '?';
		}
	}
	
	for(int i=0; i<rows; i++)
	{
		delete[] grid[i];
	}

	delete[i]
	
	return(0);
}