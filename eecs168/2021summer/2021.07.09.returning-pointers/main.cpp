#include <iostream>
void printArray(int* arrayToPrint, int size);


//Goal: Define a function that can copy an
//		array of ints and return the copy
int* copyArray(int* original, int size)
{
	int* copy = nullptr;
	
	//make a new array of the same size
	//as original
	copy = new int[size];
	
	//copy values from original into the 
	//new array
	for(int i=0; i<size; i++)
	{
		copy[i] = original[i];
	}
	
	return(copy);
}

int main()
{
	int* nums = nullptr;
	int size = 4;
	int* copyOfNums = nullptr;
	
	nums = new int[size];

	for(int i=0; i<size; i++)
	{
		nums[i] = 5;
	}		
	
	printArray( copyArray(nums,size) , size);
	
	
	copyOfNums = copyArray(nums, size);
	copyOfNums[0] = -1;
	printArray(nums, size);
	printArray(copyOfNums, size);
	//FREEZE draw call stack and heap

	delete[] nums;
	delete[] copyOfNums;
	return(0);
}

void printArray(int* arrayToPrint, int size)
{
	for(int i=0; i<size; i++)
	{
		std::cout << arrayToPrint[i] << '\n';
	}
}
