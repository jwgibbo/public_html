#include <iostream>

int main()
{
	//Goal: Create a heap-allocated array 
	//		of 4 ints
	int* nums = nullptr;
	nums = new int[4];	
	
	nums[2] = 55;
	delete[] nums;
	
	//Goal: Make 3 arrays of ints.
	//		Each array should have 4 ints
	int** grid = nullptr;
	
	//create an array of 3 pointers
	int rows = 3;
	int cols = 4;
	grid = new int*[rows];
	
	//creates an array of ints
	//for each pointers
	for(int i=0; i<rows; i++)
	{
		grid[i] = new int[cols];
	}
	
	for(int i=0; i<rows; i++)
	{
		for(int j=0; j<cols; j++)
		{
			grid[i][j] = 0;
		}
	}
	
	for(int i=0; i<rows; i++)
	{
		delete[] grid[i];
	}
	
	delete[] grid;
	
	return(0);
}