//Animal.cpp

#include "Animal.h"

Animal::Animal()
{
	std::cout << "Animal constructed\n";
}

void Animal::sleep()
{
	std::cout << "Animal is sleeping...\n";
}

void Animal::eat()
{
	std::cout << "Animal is eating...\n";
}