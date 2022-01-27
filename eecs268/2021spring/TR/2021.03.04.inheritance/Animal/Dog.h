//Dog.h

#ifndef DOG_H
#define DOG_H

#include <iostream>
#include "Animal.h"

//The Dog class inherits from Animal
//This means that A Dog is an Animal
class Dog : public Animal
{
	public:
	Dog(int age);
	virtual void sleep();
	
	void doTrick();
};


#endif