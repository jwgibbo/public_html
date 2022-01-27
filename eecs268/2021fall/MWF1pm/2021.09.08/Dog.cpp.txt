#include "Dog.h"

void Dog::doTrick()
{
	std::cout << "Trick happening\n";
}

void Dog::sleep()
{
	std::cout << "Hrp. Hrp. Hrrp. Ruf\n";
}

void Dog::eat()
{
	doTrick();
	std::cout << "Dog eating\n";
}