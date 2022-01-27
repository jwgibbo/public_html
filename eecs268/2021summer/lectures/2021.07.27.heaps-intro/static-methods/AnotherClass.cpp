#include "AnotherClass.h"

//NOTE: NO static keyword here! 
void AnotherClass::printAnInt(int num)
{
	double val = 5.5; 
	
	std::cout << "printAnInt is printing this number: ";
	std::cout << num << '\n';
	
	//DO NOT use non-static member variables
	m_instanceVariable = '?';
	
	//CAN use static member variables
	std::cout << AnotherClass::m_staticVariable << '\n';
}