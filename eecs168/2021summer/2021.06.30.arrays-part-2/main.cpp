#include <iostream>

int main()
{
	//Goal: Ask the user how many numbers
	//		they need to store. Create
	//		an array of that size
	
	//Creates an integer pointer
	//that points to null
	char* nums = nullptr;
	int userSize = 0;
	
	//Get the size from the user
	std::cout << "How many numbers do you need?: ";
	std::cin >> userSize;
	
	nums = new char[userSize];
	
	for(int i=0; i<userSize; i++)
	{
		nums[i] = '?';
	}
	
	std::cout << "Here is the array: \n";
	
	for(int i=0; i<userSize; i++)
	{
		std::cout << nums[i] << '\n';
	}
	delete[] nums;
	return(0);
}
