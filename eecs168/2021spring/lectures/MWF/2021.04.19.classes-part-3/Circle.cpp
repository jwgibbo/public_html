//Circle.cpp

#include "Circle.h"

//Define the constructor
Circle::Circle()
{
	radius = 0;
}

bool Circle::setRadius(double newRadius)
{
	if( newRadius > 0 )
	{
		radius = newRadius;
		return(true);
	}
	else
	{
		return(false);
	}
}

double Circle::getRadius()
{
	return(radius);
}

//Define area method
//Put the Circle:: only here
//in the definition
double Circle::area()
{
	double ans = 0;
	ans = 3.14*radius*radius;
	return(ans);
}