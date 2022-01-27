#include <iostream>
#include "Animal.h"
#include "Dog.h"


void playWithDog(Dog& d)
{
	d.doTrick();
}

void playWithAnimal(Animal& a)
{
	a.eat();
	a.sleep();
}

int main()
{
	Dog myDog;
	Animal myAnnie;
	
	// myAnnie.age = -1; ILLEGAL
		
	myDog.eat();
	myDog.sleep();
	playWithAnimal(myDog);	
	
	//playWithDog(myAnnie); ILLEGAL
	return(0);
}