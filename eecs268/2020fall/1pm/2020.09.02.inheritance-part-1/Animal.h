#ifndef ANIMAL_H
#define ANIMAL_H

#include <iostream>

class Animal
{
	protected:
	int age;
	bool isHungry;
	
	public:
	Animal();
	void eat();
	void sleep();
	
};

#endif