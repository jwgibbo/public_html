//main.cpp
#include <iostream>
#include "Triangle.h"//NOTE: "" not <>

int main()
{	
	Triangle myTri;
	
	//myTri.base = -10.5;
	myTri.setBase(-10.5);
	
	std::cout << myTri.getBase() << '\n';
	
	return(0);
}