//Triangle.cpp

#include "Triangle.h"

double Triangle::getBase()
{
	return(base);
}

double Triangle::getHeight()
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