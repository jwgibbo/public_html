#include <iostream>
#include "Triangle.h"

int main()
{
	Triangle triOne;
	std::string word = "dog";
	
	triOne.base = 5.5;
	triOne.height = 10.5;
	
	//Use a triangle function
	std::cout << triOne.area() << '\n';
	
	std::cout << word.length() << '\n';
	
	return(0);
}



