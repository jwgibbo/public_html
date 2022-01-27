#include <iostream>


int main()
{
	const int SIZE=5;
	int nums[SIZE];
	
	nums[0] = 55;
	nums[1] = 65;
	nums[2] = 22;
	nums[3] = 27;
	nums[4] = 865;
	
	//Goal: Print this array
	for(int i=0; i<SIZE; i++)
	{
		std::cout << nums[i] << '\n';
	}
	
	return(0);
}
