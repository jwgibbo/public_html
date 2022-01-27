#include <iostream>

void numChanger(int& num)
{
	std::cout << "AHAHAH!\n";
	num = 99;
}

int successor(int num)
{
	return(num+1);
}

//goal: define a function to print an
// array of doubles
void printArray(double* arr, int size)
{
	for(int i=0; i<size; i++)
	{
		std::cout << arr[i] << '\n';
	}
	arr = nullptr;
}	

void resetArray(double arr[], int size)
{
	for(int i=0; i<size; i++)
	{
		arr[i] = 0;
	}


	arr = new double[size];
}

int main()
{
	const int SIZE = 5;
	double nums[SIZE]; //nums refers 
						//to an array of
						//size 5
	double* heapArray = nullptr;
	heapArray = new double[SIZE];
	
	for(int i=0; i<SIZE; i++)
	{
		nums[i] = 1.5 * (i+1);
		heapArray[i] = 10 * (i+1);
	}
	
	//draw call stack prior to call
	printArray(nums, SIZE);
    printArray(heapArray, SIZE);
	return(0);
}
