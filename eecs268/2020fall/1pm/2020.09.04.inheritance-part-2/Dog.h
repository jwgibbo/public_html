#ifndef DOG_H
#define DOG_H

#include <iostream>
#include "Animal.h"

//The Dog class inherits from the 
//Animal class
class Dog : public Animal
{
	public:
	int getAge() const;
		
	void doTrick();
	void eat();
	void sleep();
	
	
	
};
#endif