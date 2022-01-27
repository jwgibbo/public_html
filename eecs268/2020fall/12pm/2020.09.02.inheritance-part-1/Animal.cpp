//Animal.cpp

#include "Animal.h"
Animal::Animal()
{
	std::cout << "Animal constructed\n";
	age = 0;
	isHungry = true;
}

void Animal::eat()
{
	std::cout << "Animal eating\n";
	isHungry = false;
}

void Animal::sleep()
{
	std::cout << "Animal sleeping\n";
	isHungry = true;
}