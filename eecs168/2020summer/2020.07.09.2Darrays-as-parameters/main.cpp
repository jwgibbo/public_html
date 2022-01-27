#include <iostream>
//Goal: Create a function that takes a 
//		2D array of doubles and initializes 
//		all values to 0
void init2D(double** arr, int rows, int cols)
{
	/*Common mistakes:
	--don't need to talk to user
	--don't need to "new" anything
	--don't need to "delete[]" anything
	*/
	for(int i=0; i<rows; i++)
	{
		for(int j=0; j<cols; j++)
		{
			arr[i][j] = 0;
		}
	}
	return;
}


int main()
{	
	double** grid = nullptr;
	double** temp = nullptr;
	int rows = 3;
	int cols = 4;
	
	//create the array of pointers
	grid = new double*[rows];
	
	//create an array of value for each 
	//pointer
	for(int i=0; i<rows; i++)
	{
		grid[i] = new double[cols];
	}
	
	//both pointers point to the same
	//thing
	temp = grid;
	grid[2][1] = 5.5;
	temp[0][3] = 9.9;
	init2D(grid, rows, cols);
	
	return(0);
}