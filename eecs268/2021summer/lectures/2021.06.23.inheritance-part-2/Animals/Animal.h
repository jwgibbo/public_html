//Animal.h
#ifndef ANIMAL_H
#define ANIMAL_H

#include <iostream>

class Animal
{
	protected:
	int m_age;

	public:
	Animal(int age);
	virtual void eat();
	virtual void sleep();
};

#endif