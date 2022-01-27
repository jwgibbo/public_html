#include <iostream>
//Goal: Define a function that
//can print the contents of an array
void printArray(double arr[], int size)
{
	arr[0] = 99;//what does this do?
	//see notes for call stack & heap
	for(int i=0; i<size; i++)
	{
		std::cout << arr[i] << '\n';
	}
}

int main()
{	
	double stackArray[4];

	double* arrPtr = nullptr;
	int size = 3;
	
	arrPtr = new double[size];
	
	//fill heap allocated array
	for(int i=0; i<size; i++)
	{
		arrPtr[i] = i*5;
	}
	
	printArray(arrPtr, size);
	
	printArray(stackArray, 4);
	
	delete[] arrPtr;
	return(0);
}