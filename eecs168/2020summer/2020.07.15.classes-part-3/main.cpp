#include <iostream>
#include <string>

//for local files, use "" instead of <>
#include "Circle.h"

int main()
{	

	Circle circA;
	Circle circB;
		
	circA.setRadius(10); //good radius
	
	
	if( circB.setRadius(-10) )
	{
		std::cout << "Radius set!\n";
	}
	else
	{
		std::cout << "Radius not set\n";
	}
	
		

	//Goal: print the area of both Circles
	std::cout << circA.area() << '\n';
	std::cout << circB.area() << '\n';
	
	
	return(0);
}