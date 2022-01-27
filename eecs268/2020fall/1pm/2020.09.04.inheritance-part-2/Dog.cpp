//Dog.cpp
#include "Dog.h"

int Dog::getAge() const
{
	return(age);
}

void Dog::doTrick()
{
	std::cout << "It's doing an amazing trick!\n";
}

void Dog::eat()
{
	std::cout << "Dog eating.\n";
}

void Dog::sleep()
{
	std::cout << "Dog sleeping.\n";
}