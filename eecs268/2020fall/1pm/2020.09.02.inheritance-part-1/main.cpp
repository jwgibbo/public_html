#include <iostream>

#include "Animal.h"
#include "Dog.h"

int main()
{
	Animal myAnnie;
	Dog myDog;
	
	myAnnie.eat();
	myAnnie.sleep();
	
	myDog.eat();
	myDog.sleep();
	
	return(0);
}