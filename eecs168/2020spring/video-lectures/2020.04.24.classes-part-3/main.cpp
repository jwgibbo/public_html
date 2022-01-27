#include <iostream>
//Note " " instead of < >
#include "Triangle.h"

/*Board work!
Revamp your Rectangle class:
1) Make length and width private
2) Add getters and setters for length and width
--Only allow positive values for length and width
--Assign to zero otherwise
3) In main, let the user provide the length and width
	for two Rectangles
4) (still in main) Print the area of the Rectangle with
	largest width
5) (still in main) Print the perimeter of the Rectangle with
	the largest length
*/

int main()
{
	//When you allocate a Triangle the 
	//constructor is 
	Triangle tri1; //Constructor is called
	Triangle tri2; //Constructor is called
	
	tri1.setBase(5.0);
	tri1.setHeight(10.0);
	
	std::cout << "Base: " << tri1.getBase() << '\n';
	std::cout << "Height: " << tri1.getHeight() << '\n';
	
	//Illegal!
	//tri1.getBase() = -5.0;
	
	std::cout << tri1.area() << '\n';
	return(0);
}