//Animal.h
#ifndef ANIMAL_H
#define ANIMAL_H

#include <iostream>

class Animal
{
	private:
	int age;

	public:
	virtual void eat();
	virtual void sleep();
};

#endif