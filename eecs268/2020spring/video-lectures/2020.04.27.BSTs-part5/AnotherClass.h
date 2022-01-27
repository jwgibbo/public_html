
#ifndef ANOTHER_CLASS_H
#define ANOTHER_CLASS_H
#include <iostream>
class AnotherClass
{
	public:
	//static methods/variables do not
	//belong to an instance
	//They belong to the entire class
	//But, they cannot refer to instance level
	//members
	static void printAnInt(int num);
	
};

#endif