//main.cpp
#include <iostream>
#include "Triangle.h"//NOTE: "" not <>

int main()
{	
	Triangle myTri; //constuctor is called
	Triangle yourTri(5.5, 8.8); //constructor called
	
	std::string word = "dog";
	
	//myTri.base = -10.5;
	myTri.setBase(10.5);
	myTri.setHeight(7.5);
	
	std::cout << myTri.getBase() << '\n';
	std::cout << myTri.getHeight() << '\n';
	
	return(0);
}