#include "AnotherClass.h"

//NOTE: no static keyword here! 
void AnotherClass::printAnInt(int num)
{
	std::cout << "printAnInt is printing this number: ";
	std::cout << num << '\n';
}