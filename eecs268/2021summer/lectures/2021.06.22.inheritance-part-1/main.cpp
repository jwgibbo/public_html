//main.cpp

#include <iostream>
#include "Animal.h"
#include "Dog.h"

//This function can only call
//Animal methods, in other words
//it can only call the methods in 
//Animal.h
void playWithAnimal(Animal& a)
{
	a.eat();
	a.sleep();
}

//You must pass in a Dog or a 
//class that inherits from Dog
void playWithDogs(Dog& d)
{
	d.eat();
	d.sleep();
	d.doTrick();
}

int main()
{
	Animal myAnimal;
	Dog myDog;
	
	playWithAnimal(myAnimal);
	playWithAnimal(myDog);
	
	playWithDogs(myDog);
	//playWithDogs(myAnimal); Error
	
	return(0);
}