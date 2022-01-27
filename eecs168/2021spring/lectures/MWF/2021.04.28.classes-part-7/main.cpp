//main.cpp
#include "CoolString.h"

int main()
{
	CoolString myCS(5);

	CoolString* heapCS = new CoolString(4);
	
	delete heapCS;
	
	return(0);	
}
