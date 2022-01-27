#include <iostream>

//Goal: Define a function that 
//		takes an array and returns
//		a pointer to a copy of it

double* copy(double* orig, int size)
{
	//create a pointer
	double* copyPtr = nullptr;
	
	//create the array
	copyPtr = new double[size];
	
	//copy all values
	for(int i=0; i<size; i++)
	{
		copyPtr[i] = orig[i];
	}
	
	//return a pointer to the copy
	return(copyPtr);
}

int successor(int n)
{
	int ans = n+1;
	return (ans);
}

int main()
{	
	double* nums = nullptr;
	double* clone = nullptr;
	int size = 4;
	int x = 0;
	
	x = successor(5);
	
	nums = new double[size];
	
	for(int i=0; i<size; i++)
	{
		nums[i] = (i+1)*5;
	}
	
	clone = copy(nums, size);
	
	delete[] nums;
	delete[] clone;
	
	return(0);
}