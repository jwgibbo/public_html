//main.cpp
#include <iostream>

#include "CoolString.h"
#include <vector>

//Define a method that takes a CoolString
//by value and prints it contents
void printCS(CoolString cs)
{
	std::cout << "Printing contents" << std::endl;
	for(int i=0; i<cs.length(); i++)
	{
		std::cout << cs.getEntry(i) << std::endl;
	}
}

int main()
{	
	//Make a stack-allocated CoolString
	//object
	CoolString myCS(4);
	CoolString* csPtr = nullptr;
	std::vector<CoolString> csVec;
	
	csPtr = new CoolString(myCS); //Calls copy constructor
	
	std::cout << std::endl;
	std::cout << "------------------" << std::endl;
	std::cout << "myCS, csPtr, and empty CoolString vector created" << std::endl;
	std::cout << "------------------" << std::endl;



	
	for(int i=0; i<myCS.length(); i++)
	{
		myCS.setEntry(i, 'S');
	}
	
	csPtr->setEntry(0, 'H');

	
	printCS(myCS);//Calls copy constructor to create cs
	printCS((*csPtr));//Calls copy constructor to create cs
	
	std::cout << std::endl;
	std::cout << "------------------" << std::endl;
	std::cout << "printCS calls done" << std::endl;
	std::cout << "------------------" << std::endl;	
	
	csVec.push_back(CoolString(77));
	csVec.push_back(CoolString(88));
	csVec.push_back(myCS);

	std::cout << std::endl;
	std::cout << "------------------" << std::endl;
	std::cout << "loading vector done" << std::endl;
	std::cout << "------------------" << std::endl;

	for (CoolString coolstring_obj : csVec)
	{
		std::cout << coolstring_obj.length() << std::endl;
	}

	std::cout << std::endl;
	std::cout << "------------------" << std::endl;
	std::cout << "printing lengths done" << std::endl;
	std::cout << "------------------" << std::endl;
	delete csPtr;
	return(0);
}


