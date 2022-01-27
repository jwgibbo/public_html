#include <iostream>

int main()
{
	int* nums = nullptr;
	int**  grid = nullptr;//all pointers can point to nullptr

	//heap allocated one dimensional array
	nums = new int[4]; //one pointer for one array

	//The size of this array determines how many
	//arrays we have
	grid = new int*[3]; //creates an array of pointers
			


	//create all the arrays of ints
	for(int i=0; i<3; i++)
	{
		//the size of these arrays determine
		//how many ints are in each array
		grid[i] = new int[4];
	}
	
	//access a specific int
	//grid[which array][which element of that array]
	grid[1][3] = 55;
	//grid is int**
	//grid[i] is int*
	//grid[i][j] is an int

	//board work: ask the user for the number of rows and cols
	//for a 2D array of doubles. Then...
	// 1) Let the user fill the array
	// 2) Print the entire array
	// 3) No memory leaks (hint: delete[] deallocates an array)
	
	return(0);
}
