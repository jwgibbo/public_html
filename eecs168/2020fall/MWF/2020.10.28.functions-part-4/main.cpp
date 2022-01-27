#include <iostream>

//GOAL: define a function that prints
//an array of ints
void printArray(int* arr, int size)
{
	arr[0] = -99;
	for(int i=0; i<size; i++)
	{
		std::cout << arr[i] << '\n';
	}
	//FREEZE POINT
	//VISUALIZE THE CALL STACK
}


int main()
{
	const int SIZE = 4;
	int nums[SIZE];
	int* heapArr = nullptr;
	
	heapArr = new int[SIZE];
	
	for(int i=0; i<SIZE; i++)
	{
		nums[i] = (i+1)*10;
		heapArr[i] = (i+1)*7;
	}
	
	printArray(nums, SIZE);
	printArray(heapArr, SIZE);
	
	return(0);
}



