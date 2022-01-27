#include <iostream>

int main()
{	
	int* nums = nullptr;
	int size = 0;
	double dubs[3];//array of 3 doubles
	
	dubs[0] = 2.5;
	dubs[1] = 3.5;
	dubs[2] = 4.5;
	
	std::cout << "How many numbers?: ";
	std::cin >> size;
	
	nums = new int[size];
	
	for(int i=0; i<size; i++)_
	{
		std::cout << "Enter a value: ";
		std::cin >> nums[i];
	}
	
	for(int i=0; i<size; i++)
	{
		std::cout << nums[i] << '\n';
	}
	
	delete[] nums;
	return(0);
}