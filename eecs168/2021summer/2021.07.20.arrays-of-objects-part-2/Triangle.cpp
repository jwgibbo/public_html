//Triangle.cpp

#include "Triangle.h"
/*
Triangle::Triangle()
{
	//Initialize your member variables
	base = 0;
	height = 0;
}
*/
Triangle::Triangle(double newBase, double newHeight)
{
	//Where's the object? 
	//We're in the object!
	setBase(newBase);
	setHeight(newHeight);
}

double Triangle::getBase() const 
{
	return(base);
}

double Triangle::getHeight() const
{
	return(height);	
}

bool Triangle::setBase(double newBase)
{
	if(newBase > 0)
	{
		base = newBase;
		return(true);
	}
	else
	{
		base = 0;
		return(false);
	}
}

bool Triangle::setHeight(double newHeight)
{
	if(newHeight > 0)
	{
		height = newHeight;
		return(true);
	}
	else
	{
		height = 0;
		return (false);
	}
}

double Triangle::area() const
{
	return(0.5*base*height);
}