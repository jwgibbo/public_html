#include <iostream>
#include "Shape.h"
#include "Circle.h"

void printShapeInfo(Shape& s)
{
	std::cout << "The area is: ";
	std::cout << s.area() << '\n';
}

int main()
{
	//Shape myShape; ILLEGAL
	Circle myCirc(10);
	Shape* sptr = new Circle(5);
	
	std::cout << "Area: ";
	std::cout << sptr->area() << '\n';
	
	printShapeInfo(myCirc);
	
	return(0);
}