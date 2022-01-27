//Animal.cpp

#include "Animal.h"

Animal::Animal(int age)
{
	std::cout << "Animal constructed\n";
	m_age = age;
}

int Animal::getAge() const
{
	return(m_age);
}

void Animal::sleep()
{
	std::cout << "Animal is sleeping...\n";
}

void Animal::eat()
{
	std::cout << "Animal is eating...\n";
}