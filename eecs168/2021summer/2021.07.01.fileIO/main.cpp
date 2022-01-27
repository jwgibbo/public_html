#include <iostream>
#include <fstream>
#include <string>

int main()
{
	std::ofstream myOutputFile;
	std::ifstream myInputFile;
	
	int size = 5;
	int* fileNums = nullptr;
	fileNums = new int[size];
	
	std::string fileName = "output.txt";
	
	//Create/open output.txt
	myOutputFile.open(fileName);
	
	//Write to output.txt
	myOutputFile << "Hello!\n";
	
	//Open the input file
	myInputFile.open("bestNumber.txt");
	
	//Read values in from file
	for(int i=0; i<size; i++)
	{
		myInputFile >> fileNums[i];
	}
	
	//print values to terminal
	for(int i=0; i<size; i++)
	{
		std::cout << fileNums[i] << '\n';
	}
	
	//close the files
	myOutputFile.close();
	myInputFile.close();
	
	//delete the array
	delete[] fileNums;
	return(0);
}