//main.cpp

#include <iostream>
#include "Animal.h"
#include "Dog.h"

void playWithAnimal(Animal& a)
{
	a.eat();
	a.sleep();
}

int main()
{
	Animal myAnimal;
	Dog myDog;
	myDog.eat();
	myDog.sleep();

	playWithAnimal(myAnimal);
	playWithAnimal(myDog);
	return(0);
}
