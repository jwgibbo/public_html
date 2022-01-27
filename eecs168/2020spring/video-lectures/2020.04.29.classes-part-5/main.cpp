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
	CoolString cs1(10);
	CoolString cs2(100);
	
	if(cs1.isSameSize(cs2))
	{
		std::cout << "Same Size!\n";
	}
	else
	{
		std::cout << "Not same size!\n";
	}
	
	
	//GOAL: Let the user pick the size of a CoolString.
	//		Allow the user to fill it with characters, //		then print them all back to the user


	//One solution: Create a heap allocated object!
	CoolString* coolPtr = nullptr;
	
	int userSize = 0;
	char temp = '\0';

	std::cout << "How big is the CoolString?: ";
	std::cin >> userSize;
	
	//After learning the size, make the CoolString
	//by making a new CoolString object
	//NOTE: This is NOT an array
	coolPtr = new CoolString(userSize); //constructor call
	
	//MEMORY VISUALIZATION #1

	//Let the user fill the CoolString
	for(int i=0; i<coolPtr->size(); i++)
	{
		std::cout << "Input a character: ";
		std::cin >> temp;
		//call setAt and pass in temp
		coolPtr->setAt(i, temp);
	}

	std::cout << "Characters stored!\n";
	
	//Print all the characters in the CoolString
	for(int i=0; i<coolPtr->size(); i++)
	{
		std::cout << coolPtr->getAt(i) << '\n';
	}
	
	delete coolPtr;
	
	return(0); 
}