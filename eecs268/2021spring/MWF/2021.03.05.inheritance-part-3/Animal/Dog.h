//Dog.h

#ifndef DOG_H
#define DOG_H

#include "Animal.h"
#include <iostream>

class Dog : public Animal
{
	public:
	Dog(int age);
	
	void doTrick();
	virtual void sleep();
};

#endif