//main.cpp
#include <iostream>
#include "CoolString.h"

int main()
{	
	CoolString myCS(5);//Create a CoolString 
					   //object		
	
	CoolString* myCSptr = nullptr;
	myCSptr = new CoolString(5);
	
	delete myCSptr;//deletes the CoolString
					//object which invokes
					//the destructor
	
	return(0);//destructor for myCS is called
}