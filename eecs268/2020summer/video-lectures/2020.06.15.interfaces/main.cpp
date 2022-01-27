//main.cpp

#include <iostream>
#include "Shape.h"
#include "Circle.h"
#include "Triangle.h"

void printArea(Shape& s)
{
	//s can only call the methods listed
	//in the Shape interface
	std::cout << "This shape's area is: ";
	std::cout << s.area() << '\n';
}

int main()
{
	Triangle tri(5, 10);
	Circle circ(10);
	
	//Illegal to construction Shape object
	//Shape s;
	
	printArea(tri);
	printArea(circ);
	
	//Board work: Define a Rectangle class 
	//that has a height and width and an area
	//method. Create a heap allocated Rectangle
	//object and pass that heap allocated object
	//to the printArea function (cannot change
	//the parameter type)
	//Rectangle* recPtr = nullptr;
	//HINT: dereference!
	
	return(0);
}