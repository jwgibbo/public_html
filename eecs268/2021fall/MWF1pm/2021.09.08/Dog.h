#ifndef DOG_H
#define DOG_H

#include "Animal.h"

class Dog : public Animal
{
	public:
	void doTrick();
	virtual void eat();
	virtual void sleep();
	
};

#endif