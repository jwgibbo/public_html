#include <iostream>

int main()
{	
	//GOAL: declare 5 ints.

	//Declare an array of integers
	const int SIZE = 5;
	int nums[SIZE];

	//Goal let the user fill the array with values:
	for(int i=0; i<SIZE; i++)
	{
		std::cout << "Input value for index " << i << ": ";
		std::cin >> nums[i];
	}
	
	for(int i=0; i<SIZE; i++)
	{
		std::cout << nums[i] << '\n';
	}
	return(0);
}