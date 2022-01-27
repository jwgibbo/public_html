#include <iostream>
#include "Animal.h"
#include "Dog.h"


int main()
{
	Dog myDog;
	Animal myAnnie;
	
	myAnnie.eat();
	myAnnie.sleep();
	
	myDog.eat();
	myDog.sleep();
	
	return(0);
}