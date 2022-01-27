#include <iostream>
void printArray(int* arr, int size);

//Goal: Define a function that takes 
//an array of ints and returns are pointer
//to a heap-allocated copy of that array
int* copyArray(int* arr, int size)
{
	int* copy = nullptr;
	
	copy = new int[size];
	
	for(int i=0; i<size; i++)
	{
		copy[i] = arr[i];
	}
	
	return(copy);
	//FREEZE: visualize memory
}

int main()
{
	const int SIZE = 4;
	int stackArr[SIZE];
	
	int* heapArr = nullptr;
	heapArr = new int[SIZE];
	
	int* copy = nullptr;
	
	for(int i=0; i<SIZE; i++)
	{
		stackArr[i] = (i+1)*5;
		heapArr[i] = (i+1)*7;
	}
	//Now main is responsible for deleting copy
	copy = copyArray(heapArr, SIZE);
	
	printArray(copy, SIZE);

	delete[] copy;	
	return(0);
}


//Goal: Define a function that
//takes an array as a parameter 
//and prints its content
void printArray(int* arr, int size)
{
	for(int i=0; i<size; i++)
	{
		std::cout << arr[i] << '\n';
	}
	//FREEZE: Visualize memory
}
