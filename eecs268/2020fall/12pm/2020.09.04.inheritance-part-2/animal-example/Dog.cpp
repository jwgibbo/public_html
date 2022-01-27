//Dog.cpp
#include "Dog.h"

Dog::Dog()
{
	age = 1;
	std::cout << "Dog constructed\n";
}

void Dog::doTrick()
{
	std::cout << "It's doing an amazing trick!\n";
}

void Dog::eat()
{
	std::cout << "Dog eating\n";
	isHungry = false;
}

void Dog::sleep()
{
	std::cout << "Dog sleeping\n";
	isHungry = true;
}