//Dog.h
#ifndef DOG_H
#define DOG_H

#include "Animal.h"

class Dog : public Animal
{
	private:
	bool m_isTired;
	
	public:
	Dog(int age);
	virtual void eat();
	virtual void sleep();
	virtual void doTrick();
	virtual void wagTail();
};

#endif