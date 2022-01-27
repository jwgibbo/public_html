#include <iostream>

void byReferenceFunc(int& n)
{
	n = -1;
}

void byValueFunc(int n)
{
	n = -1;
}

//Goal: define a function that can print
// 		an array of ints to terminal
void printArray( int* arrayToPrint, int size )
{
	arrayToPrint[0] = 99;//Hahahaha!
	for(int i=0; i<size; i++)
	{
		std::cout << arrayToPrint[i] << '\n';
	}
	size = 55;
	//FREEZE! Draw call stack and heap
	return;
}


int main()
{
	int* nums = nullptr;
	int size = 4;
	
	nums = new int[size];

	for(int i=0; i<size; i++)
	{
		nums[i] = 5;
	}		
	
	printArray(nums, size);
	byValueFunc(size); //no change to size
	byReferenceFunc(size); //change occurs
	std::cout << "nums[0] = " << nums[0] << '\n';
	std::cout << "size = " << size << '\n';
	return(0);
}