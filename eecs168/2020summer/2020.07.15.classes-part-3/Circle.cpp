//Implementation file for the Circle class
//Define all the methods for the Circle


//inclue the header file
#include "Circle.h"

Circle::Circle()
{
	//initialize member variables
	m_radius = 0;
}

//define the methods that were declared in
//the header
double Circle::area()
{
	double ans = 0;
	ans = 3.14*m_radius*m_radius;
	
	return(ans);	
}

bool Circle::setRadius(double radius)
{
	//only allow for positive values 
	//to be stored in the radius
	if(radius > 0)
	{
		m_radius = radius;
		return(true);
	}
	else
	{
		m_radius = 0;
		return(false);
	}
}

double Circle::getRadius() const 
{
	//Should this method change the radius?
	//m_radius = 5; ILLEGAL!
	return(m_radius);	
}









