#include <iostream>
#include "Circle.h"

int main()
{
	Circle circ1;
	Circle circ2;
	
	circ1.radius = 10;
	circ2.radius = 20;
	
	//print the area
	std::cout << circ1.area() << '\n';
	std::cout << circ2.area() << '\n';
	
	
	
	
}
