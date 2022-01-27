//main.cpp
#include "CoolString.h"
#include <iostream>

void printCoolString(CoolString cs)
{	
	for(int i=0; i<cs.getSize(); i++)
	{
		std::cout << cs.getEntry(i) << '\n';
	}
	cs.setEntry(0,'?');
}

int main()
{
	CoolString cs1(2);
	cs1.setEntry(0,'a');
	cs1.setEntry(1,'b');

	CoolString cs2( cs1 );//make a copy of cs1
						  //Calls copy constructor
	
	CoolString* csPtr = nullptr;
	csPtr = new CoolString(cs1);
	
	std::cout << "Printing cs1: \n";
	printCoolString(cs1);	
	std::cout << "Printing cs2: \n";
	printCoolString(cs2);
	std::cout << "Printing csPtr: \n";
	printCoolString(*csPtr);
	
	return(0);	
}
