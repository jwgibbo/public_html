#include <iostream>
#include "CoolString.h"


void someFunc()
{
	CoolString myCS(4);
	std::cout << "someFunc made another CoolString object!\n";
	//Memory visualization #2 (prior to someFunc returning)
	
	return;
}

int main()
{
	//NOTE: the myCoolString(5) is calling 
	// and passing in a parameter
	CoolString myCoolString(5);
	//Memory Visualization #1
	
	std::cout << "Hello, world!\n";
	
	someFunc();
	
	//main should NOT be responsible for deleting
	//the array
	//delete[] myCoolString.m_array; //ILLEGAL
	//delete[] myCoolString.getArray()? NO, BAD IDEA
	
	return(0); //all locally declared variables or parameters
				//are deallocated
}