#include <iostream>
#include "Shape.h"
#include "Circle.h"

void printShapeInfo(Shape& s)
{
	std::cout << "The area = ";
	std::cout << s.area() << '\n';
}

int main()
{
	Circle myCirc(10);
	Shape* sptr = nullptr;
	
	sptr = new Circle(5.5);
	std::cout << "Area = " << sptr->area();
	std::cout << std::endl; 
	
	printShapeInfo(myCirc);
	
	return(0);
}