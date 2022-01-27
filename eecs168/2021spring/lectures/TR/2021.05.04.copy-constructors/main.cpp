//main.cpp

#include "CoolString.h"
#include <iostream>

//passing by value invoke the Copy Constructor
void printCS( CoolString cs )
{
	for(int i=0; i<cs.getSize(); i++)
	{
		std::cout << cs.getEntry(i) << '\n';
	}
}

int main()
{
	CoolString cs1(2);
	CoolString cs2(2);
	
	cs1.setEntry(0,'a');
	cs1.setEntry(1,'b');
	cs2.setEntry(0,'x');
	cs2.setEntry(1,'y');
	
	CoolString csCopy( cs2 );//makes a copy
	csCopy.setEntry(0, '?');
	
	std::cout << "Printing original: \n";
	printCS(cs1);
	std::cout << "Printing copy: \n";
	printCS(csCopy);
	
	if( cs1 == cs2 )
	{
		//do something
	}
	
}