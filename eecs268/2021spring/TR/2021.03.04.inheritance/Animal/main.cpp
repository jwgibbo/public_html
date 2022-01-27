//main.cpp

#include <iostream>

#include "Animal.h"
#include "Dog.h"

void printAnimal( Animal& a )
{
	std::cout << "Age: " << a.getAge() << '\n';
	a.sleep();
	//a.doTrick(); ILLEGAL
}

int main()
{	
	Animal myAnimal(5);
	Dog myDog(13);
	
	//print the ages
	printAnimal(myAnimal);
	printAnimal(myDog);

	//myAnimal.sleep();
	//myDog.sleep();
	myDog.doTrick();
	//myAnimal.doTrick(); ILLEGAL
	return(0);
}