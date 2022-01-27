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
	Animal myAnimal(3);
	Dog myDog(7);//calls Animal constructor
	std::cout << "Animal's age: " << myAnimal.getAge() << '\n';
	std::cout << "Dog's age: " << myDog.getAge() << '\n';
	return(0);
}







