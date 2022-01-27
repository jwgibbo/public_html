#include <iostream>

int main()
{
	//Goal: Obtain 5 ints from the user
	const int SIZE=7;
	int nums[SIZE];
	
	for(int i=0; i<SIZE; i++)
	{
		std::cout << "Input a value for index ";
		std::cout << i << ": ";
		std::cin >> nums[i];
	}
	
	for(int i=0; i<SIZE; i++)
	{
		std::cout << nums[i] << '\n';
	}
	
	std::cout << "nums=" << nums << '\n';
	return(0);
}