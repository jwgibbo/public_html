#include <iostream>

#include "CoolString.h"

int main()
{	
	//Make a stack-allocated CoolString
	//object
	CoolString myCS(4);
	CoolString* csPtr = nullptr;
	
	csPtr = new CoolString(3);
	
	delete csPtr;//calls destructor
	
	//right before main is over,
	//we no longer need myCS's array
	//Stack allocated myCS object's 
	//destructor is called when main 
	//returns
	return(0);
}