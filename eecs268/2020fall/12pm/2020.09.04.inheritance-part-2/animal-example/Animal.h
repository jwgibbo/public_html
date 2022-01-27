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
	virtual void eat();
	virtual void sleep();
};

#endif