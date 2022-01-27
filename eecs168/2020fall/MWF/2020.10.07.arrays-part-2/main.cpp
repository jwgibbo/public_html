#include <iostream>

int main()
{
	int* nums = nullptr;
	int userSize = 0;
	
	std::cout << "Input a size: ";
	std::cin >> userSize;
	
	nums = new int[userSize];
	
	//Use the array as normal	
	nums[0] = 55;
	
	
	//after you don't need the array, delete it
	delete[] nums;
	return(0);
}