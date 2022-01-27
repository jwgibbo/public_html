#include <iostream>

//Goal: Define a function that prints
//the contents of an array
void arrayPrint(int* arr, int size)
{
	arr[0] = -100;
	//See notes for memory visualization
	for(int i=0; i<size; i++)
	{
		std::cout << arr[i] << '\n';
	}
}

int main()
{
	int* nums = nullptr;
	int size = 4;
	
	nums = new int[size];
	for(int i=0; i<size; i++)
	{
		nums[i] = (i+1)*7;
	}
	
	arrayPrint(nums, size);
	
	for(int i=0; i<size; i++)
	{
		std::cout << nums[i] << '\n';
	}
	
	return(0);
}
