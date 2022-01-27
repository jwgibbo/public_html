#include <iostream>

int main()
{	
	//This program causes a memory leak:
	
	int* nums = nullptr;
	int userSize = 0;
	
	std::cout << "How many numbers?: ";
	std::cin >> userSize;
	
	nums = new int[userSize];
	
	//run with 
	//valgrind --leak-check=full ./prog
	
	return(0);
}