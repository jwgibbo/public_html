#include <iostream>
#include "CoolString.h"

int main()
{	
	//Make a stack-allocated CoolString
	//object
	CoolString coolWord1(4);
	CoolString coolWord2(4);
	coolWord1.setEntry(0, 'Q');
	
	if( coolWord1 != coolWord2 )
	{
		std::cout << "No match\n";
	}
	else
	{
		std::cout << "Match\n";
	}

	return(0);
}






