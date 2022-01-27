#include <iostream>
#include "CoolString.h"


void printACoolString(const CoolString& cs)
{
	//print the contents of cs
	for(int i=0; i<cs.size(); i++)
	{
		std::cout << cs.getAt(i) << '\n';
	}	
	return;//optional 
}

int main()
{	
	CoolString coolWord1(5);
	CoolString coolWord2(5);
	
	//Fill the cool string's array with Ms
	for(int i=0; i<coolWord1.size(); i++)
	{
		coolWord1.setAt(i, 'M');
		coolWord2.setAt(i, 'M');
	}
	
	//coolWord2.setAt( (coolWord2.size()-1) , 'Z');
	
	//Pass to function for printing
	
	std::cout << "Printing word 1:\n";
	printACoolString(coolWord1);
	
	std::cout << "Printing word 2:\n";
	printACoolString(coolWord2);
	
	//compare using == operator
	if(coolWord1 == coolWord2)
	{
		std::cout << "They match!\n";
	}
	else
	{
		std::cout << "They don't match!\n";
	}
	
	if(coolWord1 != coolWord2)
	{
		std::cout << "They don't match!\n";
	}
	else
	{
		std::cout << "They match!\n";
	}
	
	return(0); 
}