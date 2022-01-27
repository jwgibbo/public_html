#include <iostream>

int main()
{
	//Goal get 5 ints from the user
	
	const int SIZE = 5;
	int nums[SIZE];
	
	nums[0] = 42;
	nums[1] = 33;
	nums[2] = 55;
	
	std::cout << nums[2] << '\n';
	
	return(0);
}