//Animal.cpp

#include "Animal.h"

Animal::Animal(int age)
{
	std::cout << "Animal constructed\n";
	m_age = age;
	m_isHungry = true;
}

int Animal::getAge() const
{
	return(m_age);
}

void Animal::sleep()
{
	std::cout << "Animal sleeping...\n";
}