//main.cpp
#include "CoolString.h"
#include <iostream>
int main()
{
	std::string word = "dog";
	std::string word2 = "banana";
	std::cout << word.length() << '\n';
	std::cout << word2.length() << '\n';
	
	
	CoolString cs1(2);
	CoolString cs2(2);
	
	cs1.setEntry(0,'a');
	cs1.setEntry(1,'b');

	cs2.setEntry(0,'a');
	cs2.setEntry(1,'b');
	
	if(cs1 == cs2)
	{
		std::cout << "Equal!\n";
	}
	
	
	return(0);	
}
