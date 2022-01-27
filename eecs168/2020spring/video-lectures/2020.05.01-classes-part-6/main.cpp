#include <iostream>
#include "CoolString.h"

void byValueTest(CoolString cs)
{
	//print the contents of cs
	for(int i=0; i<cs.size(); i++)
	{
		std::cout << cs.getAt(i) << '\n';
	}
	
	//MEMORY VISUALIZATION #2 and #3
	//#2 is before we defined the copy constructor
	//#3 is after we defined the copy constructor 
	return;//optional
}

void printACoolString(const CoolString& cs)
{
	//print the contents of cs
	for(int i=0; i<cs.size(); i++)
	{
		// cs.setAt(i,'Z'); ILLEGAL since it's not const
		std::cout << cs.getAt(i) << '\n';
	}

	//MEMORY VISUALIZATION #1
	
	return;//optional 
}

int main()
{	
	CoolString myCoolString(5);
	
	//Fill the cool string's array with Ms
	for(int i=0; i<myCoolString.size(); i++)
	{
		myCoolString.setAt(i, 'M');
	}
	
	//Pass to function for printing
	//printACoolString(myCoolString);
	
	byValueTest(myCoolString);
	
	return(0); 
}