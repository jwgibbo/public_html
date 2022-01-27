#include <iostream>

int main()
{
	//PLEASE NOTE the video had this as int*
	//it should be double**
	double**  grid = nullptr;//all pointers can point to nullptr

	int numRows=0;
	int numCols=0;

	//board work: ask the user for the number of rows and cols
	//for a 2D array of doubles. Then...
	// 1) Let the user fill the array
	// 2) Print the entire array
	// 3) No memory leaks (hint: delete[] deallocates an array)
	
	std::cout << "How many rows?: ";
	std::cin >> numRows;
	std::cout << "How many cols?: ";
	std::cin >> numCols;
	
	//create the array of pointers
	//CORRECTION: video has new int* arrays
	grid = new double*[numRows];
	
	for(int i=0; i<numRows; i++)
	{
		//CORRECTION: video makes arrays of ints
		grid[i] = new double[numCols];
	}
	
	for(int i=0; i<numRows; i++)
	{
		for(int j=0; j<numCols; j++)
		{
				std::cout << "Input value for row " << i;
				std::cout << " column " << j << ": ";
				std::cin >> grid[i][j];
		}
	}
	
	for(int i=0; i<numRows; i++)
	{
		for(int j=0; j<numCols; j++)
		{
				std::cout << grid[i][j] << " ";
		}
		std::cout << "\n";
	}
	
	//delete the each array of ints
	for(int i=0; i<numRows; i++)
	{
		delete[] grid[i];
	}
	
	delete[] grid;
	
	/* Board work!
	1) Let the user pick the dimensions for an array of doubles. Then
		ask them which column they want to print. (Assume they know column 
		indexing starts at 0). Print you that column with each value on its own
		line.
		
		After that print the following information about the array:
		1b) Sum of all values
		1c) Average value
		1d) Largest value
	*/
	
	
	return(0);
}
