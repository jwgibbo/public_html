#include <iostream>
#include "Triangle.h"

int main()
{

	Triangle triOne;
	Triangle triTwo;
	
	triOne.base = 5.5;
	triOne.height = 10.5;
	
	triTwo.base = 2;
	triTwo.height = 4;
	
	//print the area of triOne
	std::cout << triOne.area() << '\n';
	std::cout << triTwo.area() << '\n';
	return(0);
}
