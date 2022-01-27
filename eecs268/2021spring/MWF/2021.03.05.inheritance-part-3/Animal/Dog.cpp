//Dog.cpp

#include "Dog.h"

                   //initializer list
Dog::Dog(int age) : Animal(age)
{
	std::cout << "Dog constructed!\n";
	m_isHungry = false;
}

void Dog::doTrick()
{
	std::cout << "Dog is rolling over\n";
}

void Dog::sleep()
{
	std::cout << "Rup. Rup. Rup-up\n";
}