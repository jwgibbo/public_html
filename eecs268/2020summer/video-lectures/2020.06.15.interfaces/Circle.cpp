//Circle.cpp

#include "Circle.h"

Circle::Circle(double radius)
{
	m_radius = radius;
}

double Circle::area() const
{
	//area = pi*r^2
	return(3.14159*m_radius*m_radius);
}