//Implementation file for the Circle class
//Define all the methods for the Circle


//inclue the header file
#include "Circle.h"

//define the methods that were declared in
//the header
double Circle::area()
{
	double ans = 0;
	ans = 3.14*radius*radius;
	
	return(ans);	
}