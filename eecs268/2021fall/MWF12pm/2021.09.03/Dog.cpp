#include "Dog.h"

void Dog::doTrick()
{
	std::cout << "Trick occuring.\n";
}

void Dog::eat()
{
	doTrick();
	std::cout << "Dog eating...\n";
}

void Dog::sleep()
{
	std::cout << "Dog sleeping...\n";
}
