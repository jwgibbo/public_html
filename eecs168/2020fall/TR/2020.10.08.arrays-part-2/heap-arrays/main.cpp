#include <iostream>

int main()
{
	int* nums = nullptr;

	int userSize = 0;
	
	std::cout << "Input a size: ";
	std::cin >> userSize ;
	
	nums = new int[userSize];
	
	nums[0] = 55;
	
	//after we're done with the arrray
	//delete it
	delete[] nums;
	return(0);
}