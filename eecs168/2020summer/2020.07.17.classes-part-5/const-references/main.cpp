#include <iostream>
#include <string>

//for local files, use "" instead of <>
#include "Circle.h"

//NOTE: printCircle is NOT
//a member of circle class!
void printCircle(const Circle& c)
{
	std::cout << "radius is: ";
	std::cout << c.getRadius() << '\n';
	std::cout << "area is: ";
	std::cout << c.area() << '\n';
}

int main()
{	

	Circle circ;
	Circle* cPtr = nullptr;
	
	circ.setRadius(10); //good radius
	
	cPtr = new Circle();	
	cPtr->setRadius(5);
	
	printCircle(circ);
	printCircle( (*cPtr) );
	
	delete cPtr;
	
	return(0);
}