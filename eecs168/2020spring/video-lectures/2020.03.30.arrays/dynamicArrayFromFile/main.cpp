#include <iostream>
#include <fstream>

/* file format:

<number of entries>
<entry1>
<entry2>
...
<entryN>
*/

int main()
{
	int numEntries = 0;
	int* nums = nullptr;
	std::ifstream inFile;
	std::string fileName = "";
	
	std::cout << "Which file has the data?: ";
	std::cin >> fileName;
	
		
	inFile.open(fileName);
	
	
	//Was the file opened successfully?
	if( inFile.is_open() )
	{
		inFile >> numEntries;
		std::cout << "There are " << numEntries << " in the file.\n";
		
		nums = new int[numEntries];
		
		for(int i=0; i<numEntries; i++)
		{
			inFile >> nums[i];
			
			std::cout << "Entry #" << (i+1) << " " << nums[i] << "\n";
		}
		
		//do stuff with numbers
		
		
		delete[] nums;
		
	}
	else
	{
		std::cout << "ERROR: File could not found\n";
	}
	
	
	return(0);
}