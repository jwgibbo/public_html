#include <iostream>

#include "Animal.h"
#include "Dog.h"

void playWithDog(Dog& d)
{
	d.eat();
	d.sleep();
	d.doTrick();
}

void playWithAnimal(Animal& a)
{
	a.eat();
	a.sleep();
	// a.doTrick(); ILLEGAL
}

int main()
{
	Animal myAnnie;
	Dog myDog;

	myDog.eat();
	myDog.sleep();
	playWithAnimal(myDog);

	// playWithDog(myAnnie); ILLEGAL 
	return(0);
}