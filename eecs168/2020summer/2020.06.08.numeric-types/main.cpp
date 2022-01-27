#include <iostream>

int main()
{
	double pi = 3.14159;
	double radius = 0;
	double area = 0;
	//GOAL: let the user give you a radius
	//		then show them the area of that 
	//		circle
	
	std::cout << "Input a radius: ";
	std::cin >> radius;
	
	//Area of a circle: pi*r^2, but 
	//we don't have exponent!
	area = pi*radius*radius;
	
	std::cout << "Area : " << area << "\n";
	
	
	
	return(0);
}

/* Board work:
1) Create a main.cpp that does the following:
Let the user pick the base and height for a 
triangle. 
Then, display the area of that triangle.

2) Create a main.cpp that asks the user for
	their current account balance. Then for an
	amount to withdraw from that account. 
	After they withdraw the money, show them
	the new balance (negative balances allowed)
*/
