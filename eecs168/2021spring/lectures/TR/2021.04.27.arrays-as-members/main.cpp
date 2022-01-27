//main.cpp

#include "CoolString.h"

int main()
{
	CoolString myCS(4);
	CoolString* coolPtr = nullptr;
	
	coolPtr = new CoolString(3);
	delete coolPtr; //calls destructor
					//for the heap allocated
					//object
	
	return(0);//main returns invokes 
				//destructor for myCS
}