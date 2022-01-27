//main.cpp

#include "CoolString.h"
#include <iostream>
int main()
{
	CoolString cs1(2);
	CoolString cs2(2);
	
	cs1.setEntry(0,'a');
	cs1.setEntry(1,'b');
	
	std::cout << cs1.getSize() << '\n';
	
	cs2.setEntry(0,'a');
	cs2.setEntry(1,'b');
	
	if( cs2 == cs1 )
	{
		std::cout << "Equal!\n";
	}
	
}