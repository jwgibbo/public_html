#include <iostream>

//Function declarations
void fillMultTwos(int* arr, int size);
void arrayPrint(int arr[], int size);


int main()
{
	int* nums = nullptr;
	int size = 4;
	const int SIZE = 10;
	int stackArray[SIZE];
	
	nums = new int[size];
	fillMultTwos(nums, size);	
	arrayPrint(nums, size);	
	
	std::cout << "=======\n";
	
	fillMultTwos(stackArray, SIZE);
	arrayPrint(stackArray, SIZE);
	
	delete[] nums;
	
	return(0);
}

void fillMultTwos(int* arr, int size)
{
	for(int i=0; i<size; i++)
	{
		arr[i] = (i+1)*2;
	}
}

void arrayPrint(int arr[], int size)
{
	//Draw the call stack and heap
	for(int i=0; i<size; i++)
	{
		std::cout << arr[i] << '\n';
	}
}
