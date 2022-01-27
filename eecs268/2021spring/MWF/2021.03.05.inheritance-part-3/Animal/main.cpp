//main.cpp

#include <iostream>

#include "Animal.h"
#include "Dog.h"

//An Animal& or Animal* only has access
//to Animal methods
void printAnimal(Animal& a)
{
	std::cout << "Animal's age: ";
	std::cout << a.getAge() << '\n';
	a.sleep(); //POLYMORPHISM!
	//a.doTrick(); ILLEGAL
}

int main()
{	
	Animal myAnimal(7);
	Dog myDog(12);
	
	//myAnimal.doTrick();
	myDog.doTrick();
	myDog.sleep();
	
	printAnimal( myAnimal );
	printAnimal( myDog );
	return(0);
}