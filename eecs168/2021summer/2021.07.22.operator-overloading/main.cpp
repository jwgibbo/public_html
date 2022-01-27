//main.cpp
#include <iostream>
#include "Triangle.h"//NOTE: "" not <>

int main()
{	
	Triangle tri1(100,200);
	Triangle tri2(50,100);
	
	std::cout << tri1.area() << '\n';
	std::cout << tri2.area() << '\n';
	
		
	if(tri2 < tri1)
	{
		std::cout << "tri2 is bigger\n";
	}
	else
	{
		std::cout << "tri1 is bigger\n";
	}
	
	return(0);
}