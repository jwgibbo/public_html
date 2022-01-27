#include <iostream>

void printArr(int arr[], int size)
{
	//base case
	if(size == 1)
	{
		std::cout << arr[0] << '\n';
	}
	//take a piece out of the whole problem
	//and hand the rest of the problem to the
	//recursive call
	else
	{
		std::cout << arr[0] << '\n';
		printArr(arr+1, size-1);
	}
}



int main()
{
	int size = 4;
	int* nums = new int[size];
	
	for(int i=0; i<size; i++)
	{
		nums[i] = (i+1)*10;
	}
	
	printArr(nums, size);

	return(0);
}