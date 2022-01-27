#include <iostream>

#include "CoolString.h"

//Define a method that takes a CoolString
//by value and prints it contents
void printCS(CoolString cs)
{
	for(int i=0; i<cs.length(); i++)
	{
		std::cout << cs.getEntry(i) << '\n';
	}
}

int main()
{	
	//Make a stack-allocated CoolString
	//object
	CoolString myCS(4);
	CoolString* csPtr = nullptr;
	
	csPtr = new CoolString(3);
	
	myCS.setEntry(0, 'S');
	
	csPtr->setEntry(0, 'H');
	
	printCS(myCS);
	printCS(myCS);
	delete csPtr;//calls destructor
	return(0);
}






