#include <iostream>
#include <fstream>

int main()
{	
	//Goal: Store values from file in an array.
	
	//Declare an input file object
	std::ifstream myInFile;
	double* nums = nullptr;
	int size = 0; 
	
	//open the input file
	//NOTE: This file needs to already exist!
	myInFile.open("nums.txt");
	
	//Check if file was opened
	if( myInFile.is_open())
	{
		std::cout << "It's open!\n";
		
		//read in the array size
		myInFile >> size;
		
		//create the array
		nums = new double[size];
		
		//read in all the values
		for(int i=0; i<size; i++)
		{			
			myInFile >> nums[i];
		}
		
		//For demo purposes print the values:
		for(int i=0; i<size; i++)
		{
			std::cout << nums[i] << '\n';
		}
		
		//Maybe use
		//print (*pointerName)@arraySize
		//in gdb
	}
	else
	{
		std::cout << "File not found!\n";
	}
	
	return(0);
}