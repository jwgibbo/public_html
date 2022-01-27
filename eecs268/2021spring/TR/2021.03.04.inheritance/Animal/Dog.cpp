//Dog.cpp
#include "Dog.h"


           //Initializer list
Dog::Dog(int age) : Animal(age)
{
	std::cout << "Dog constructed\n";
	//m_age is assigned in Animal constructor
	m_isHungry = false;
}

void Dog::sleep()
{
	std::cout << "Rup. Rup-rup. Rup\n";
}

void Dog::doTrick()
{
	std::cout << "Dog rolls over.\n";
}