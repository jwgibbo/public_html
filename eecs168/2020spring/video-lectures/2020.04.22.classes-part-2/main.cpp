#include <iostream>
//Note " " instead of < >
#include "Triangle.h"

/* 
1) Create a Rectangle.h
-Rectangles have a length and width
-Have methods to calculate area and perimeter 

2) In main, ask the user for the length and width of a rectangle and print its area and permiter using your member methods!
*/


int main()
{
	//When you allocate a Triangle the 
	//constructor is 
	Triangle tri1; //Constructor is called
	Triangle tri2; //Constructor is called
	
	std::cout << "Base and height of newly constructed tri1: " << tri1.base << ' ' << tri1.height << '\n';
	
	std::cout << "Enter base and height:";
	std::cin >> tri1.base >> tri1.height;
	
	std::cout << "Enter base and height:";
	std::cin >> tri2.base >> tri2.height;

	//Call the area method that belongs to all 
	//Triangles using tri1
	std::cout << "Area for tri1: " << tri1.area();
	std::cout << std::endl;
	
	//Call the area method that belongs to all 
	//Triangles using tri2
	std::cout << "Area for tri2: " << tri2.area();
	std::cout << std::endl;
	
	return(0);
}