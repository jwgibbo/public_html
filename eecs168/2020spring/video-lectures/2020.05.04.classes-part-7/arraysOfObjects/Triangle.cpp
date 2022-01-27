
//cpp files for classes are implementation files
//All methods are defined in the cpp file


//First thing to do in cpp is include the header file
#include "Triangle.h"

Triangle::Triangle(double b, double h)
{
	//Assigning base and height initial values
	base = b;
	height = h;
}

//This method belongs to the Triangle
double Triangle::area()
{
	//base and height's values will be 
	//determined based on which instance/object
	//is doing the calling
	double ans = 0;
	ans = 0.5*base*height;
	return(ans);
}

void Triangle::setBase(double b)
{
	if(b > 0)
	{
		base = b;
	}
	else
	{
		base = 0;
	}
}

void Triangle::setHeight(double h)
{
	if(h > 0)
	{
		height = h;
	}
	else
	{
		height = 0;
	}
}

double Triangle::getBase()
{
	return(base);
}

double Triangle::getHeight()
{
	return(height);
}