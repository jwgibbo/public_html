#include <iostream>

int main()
{	
	const int SIZE = 5;
	int nums[SIZE];
	
	nums[0] = 17; //stores 17 at index 0	
	nums[1] = 55;
	nums[2] = 195;
	nums[3] = 22;
	nums[4] = 99;
	
	//use this array with a loop
	//Goal: print all values in the array
	
	for(int i=0; i<SIZE; i++)
	{
		std::cout << nums[i] << '\n';
	}
	
	
	
	return(0);
}