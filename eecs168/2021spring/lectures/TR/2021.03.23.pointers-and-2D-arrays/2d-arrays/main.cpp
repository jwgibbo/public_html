#include <iostream>


int main()
{
	//Goal: Make a 3x4 grid of ints	
	int** grid = nullptr;
	
	grid = new int*[3];
	
	for(int i=0; i<3; i++)
	{
		grid[i] = new int[4];
	}
	
	grid[1][3] = 5;
	
	//just prints random memory address
	std::cout << grid << '\n';
	
	return(0);
}
