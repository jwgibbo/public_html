#include <iostream>

int factorial(int n)
{
	//base case
	if( n <= 1)
	{
		return( 1 );
	}
	else
	{
		//5! ==> 5*4*3*2*1
		//5! ==> 5*4!
		//4! ==> 4*3!
		//3! ==> 3*2!
		//2! ==> 2*1!
		//1! ==> 1
		return(n*factorial(n-1));
	}
}


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
		printArr(arr, size-1);
		std::cout << arr[size-1] << '\n';
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