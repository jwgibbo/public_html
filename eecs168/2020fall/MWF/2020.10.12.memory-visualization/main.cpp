#include <iostream>

int main()
{
	int num = 5;	
	int size = 4;
	int stackArr[3];
	
	int* ptr = nullptr;
	
	//everything allocated using new
	//is allocated on the heap
	ptr = new int[size];
	
	//Create a "2D" array
	
	//First, create a pointer that wiill
	//point to an an array of pointers
	int** grid = nullptr;
	int rows = 3;
	int cols = 4;
	int userNum = 0;
	//create the array of pointers
	grid = new int*[rows];
	
	//create arrays of integer for all pointers
	for(int i=0; i<rows; i++)
	{	
		grid[i] = new int[cols];
	}
	
	grid[1][2] = 55;
	
	//fill the array with values from the 
	//user
	for(int i=0; i<rows; i++)
	{
		for(int j=0; j<cols; j++)
		{
			std::cout << "Enter a value: ";
			std::cin >> grid[i][j];	
		}
	}
	
	//delete all array
	//first delete the arrays of integers
	for(int i=0; i<rows; i++)
	{
		delete[] grid[i];
	}
	//lastly, delete the array of pointers
	delete[] grid;
	
	return(0);
}