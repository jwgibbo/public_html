//Triangle.cpp
#include "Triangle.h"
//Define the member methods
//for the Triangle class

double Triangle::area()
{
	//This method has
	//access to all members
	//of the Triangle class
	double ans = 0;
	ans = 0.5*base*height;
	return (ans);
}