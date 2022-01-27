//Animal.h

#ifndef ANIMAL_H
#define ANIMAL_H

#include <iostream>

class Animal
{
	public:
	Animal(int age);
	int getAge() const;	
	virtual void sleep();
	
	protected:
	int m_age;
	bool m_isHungry;
	
	
};

#endif