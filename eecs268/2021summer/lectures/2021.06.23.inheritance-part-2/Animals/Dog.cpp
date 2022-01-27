//Dog.cpp

#include "Dog.h"

                //Initializer list
Dog::Dog(int age) : Animal(age)
{
	m_isTired = true;
	std::cout << "Dog constructor\n";
}

void Dog::sleep()
{
	std::cout << "Dog is sleeping. Woof.\n";
	m_isTired = false;
	m_age = m_age+1;
	std::cout << "Is the dog tired: ";
	std::cout << m_isTired << '\n';
}

void Dog::eat()
{
	wagTail();
	std::cout << "Dog is sitting and begging for food.\n";
}

void Dog::doTrick()
{
	std::cout << "The Dog rolled over\n";
}

void Dog::wagTail()
{
	std::cout << "The Dog is waggin its tail\n";
}