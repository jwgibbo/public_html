#include <iostream>
int* arrayCopy(int* orig, int size)
{
	int* copy = nullptr;
	copy = new int[size];
	
	for(int i=0; i<size; i++)
	{
		copy[i] = orig[i];
	}
	return(copy);
}

int main()
{
	int* nums = nullptr;
	int size = 5;
	int* copy = nullptr;
	
	nums = new int[size];
	
	for(int i=0; i<size; i++)
	{
		nums = (i+1)*21;
	}	
	copy = arrayCopy(nums, size);
	delete[] nums;
	delete[] copy;

	return(0);
}



