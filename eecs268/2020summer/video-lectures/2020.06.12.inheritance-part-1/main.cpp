//main.cpp

#include <iostream>
#include "Animal.h"
#include "Dog.h"

void playWithAnimal(Animal& theAnimal)
{
	theAnimal.eat();
	theAnimal.sleep();
	//theAnimal.doTrick(); ERROR
}

int main()
{
	Animal a;
	Dog d;
	Dog* dptr = new Dog();
	Animal* aptr = nullptr;

	dptr->doTrick();
	dptr->eat(); //Dog definition

	aptr = dptr; //Both pointing to same Dog object
	aptr->sleep(); //Dog defintion

	return(0);
}