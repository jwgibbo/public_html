//main.cpp
#include <iostream>

#include "CoolString.h"
#include <vector>

//Define a method that takes a CoolString
//by value and prints it contents
void printCS(CoolString& cs)
{
	std::cout << "Printing contents" << std::endl;
	if (cs.length() > 0)
	{
		for(int i=0; i<cs.length(); i++)
		{
			std::cout << cs.getEntry(i) << std::endl;
		}
	}
	else
	{
		std::cout << "CoolString empty" << std::endl;
	}
}

int main()
{	
	//Make a stack-allocated CoolString
	//object
	CoolString myCS(4);
	CoolString* csPtr = new CoolString(4);
	std::vector<CoolString> csVec;
	
	for(int i=0; i<myCS.length(); i++)
	{
		myCS.setEntry(i, 'S');
		csPtr->setEntry(i, 'H');
	}
		
	printCS(myCS);
	printCS((*csPtr));
	
	myCS = *csPtr; //Deep copy assignment
	
	printCS(myCS);
	printCS((*csPtr));
	
	myCS = std::move(*csPtr); //Move assignment
	
	printCS(myCS);
	printCS((*csPtr)); //This is has been moved, so its empty
	
	delete csPtr; //We still delete pointer to moved items
				  //because the move deals with members, not the 
				  //containing object
	return(0);
}


