#include <iostream>
#include <string>

//for local files, use "" instead of <>
#include "Circle.h"

int main()
{	
	Circle circA;
	Circle circB;
	
	circA.radius = 10;
	circB.radius = 5;
	
	//Goal: print the area of both Circles
	std::cout << circA.area() << '\n';
	std::cout << circB.area() << '\n';

	
	return(0);
}