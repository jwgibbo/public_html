//Circle.cpp
#include "Circle.h"

Circle::Circle(double radius)
{
	m_radius = radius;
}

double Circle::circumference() const
{
	return(2*3.14*m_radius);
}

//Satifies the requirement from the 
//Shape class
double Circle::area() const
{
	return(3.14*m_radius*m_radius);
}