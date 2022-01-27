//main.cpp

#include <iostream>
#include "Animal.h"
#include "Dog.h"

void playWithAnimal(Animal& a)
{
	a.eat();
	a.sleep();
	//a.doTrick();//ERROR
}

int main()
{
	Animal myAnimal;
	Dog myDog;
	playWithAnimal(myDog);
	return(0);
}