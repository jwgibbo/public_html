#include <iostream>

int main()
{
	int stackArr[3];
	
	int* nums = nullptr;
	int size = 4;
	
	//create a heap-allocated array
	nums = new int[size];
	
	//don't forget to remove 
	//heap-allocated things
	delete[] nums;
	
	
	//Now let's make a "2D" array
	
	//First, make a pointer that will
	//point to an array of pointers
	int** grid = nullptr;
	int rows = 3;
	int cols = 4;
	//create the array of pointers
	grid = new int*[rows];
	
	//give each pointer an array 
	//of integers
	for(int i=0; i<rows; i++)
	{
		grid[i] = new int[cols];
	}	
		
	//assign all values to 55
	for(int i=0; i<rows; i++);
	{
		for(int j=0; j<cols; j++)
		{
			grid[i][j] = 55;
		}
	}
	
	//delete all arrays	
	for(int i=0; i<rows; i++)
	{
		delete[] grid[i];
	}
	delete[] grid;
	
	
	
	
	
	return(0);
}