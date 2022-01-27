//Triangle.cpp
#include "Triangle.h"

Triangle::Triangle()
{
	//Assigning base and height initial values
	m_base = 0;
	m_height = 0;
}

//This method belongs to the Triangle
double Triangle::area()
{
	//base and height's values will be 
	//determined based on which instance/object
	//is doing the calling
	double ans = 0;
	ans = 0.5*m_base*m_height;
	return(ans);
}

double Triangle::getBase()
{
	return(m_base);
}

double Triangle::getHeight()
{
	return(m_height);
}

bool Triangle::setBase(double base)
{
	if(base>0)
	{
		m_base = base;
		return(true);
	}
	else
	{
		return(false);
	}
	
}

bool Triangle::setHeight(double height)
{
	if(height>0)
	{
		m_height = height;
		return(true);
	}
	else
	{
		return(false);
	}
	
}










