//main.cpp

#include <iostream>

#include "Animal.h"
#include "Dog.h"

void printAnimal(Animal& a)
{
	//std::cout << "age = " << a.m_age << '\n';
	//std::cout << "hungry? = " << a.m_isHungry << '\n';
}

int main()
{	
	Animal myAnimal;
	Dog myDog;
	
	//Illegal now that they are protected
	//myAnimal.m_age = 10;
	//myAnimal.m_isHungry = false;
	
	//myDog.m_age = 55;
	//myDog.m_isHungry = true;
	
	printAnimal(myAnimal);
	printAnimal(myDog);
	
	return(0);
}