//main.cpp
#include <iostream>
#include "Circle.h"

int main()
{
	Circle circ1;//Constructor is called
	Circle circ2;//Constructor is called
	
	std::cout << circ1.getRadius() << '\n';
	std::cout << circ2.getRadius() << '\n';
	
	circ1.setRadius(20);
	circ2.setRadius(-10);
	
	//print the area
	std::cout << circ1.area() << '\n';
	std::cout << circ2.area() << '\n';
	
}
