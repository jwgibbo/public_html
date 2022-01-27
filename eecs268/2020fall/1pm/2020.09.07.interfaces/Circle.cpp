//Circle.cpp
#include "Circle.h"

Circle::Circle(double radius)
{
	m_radius = radius;
}

double Circle::area() const
{
	return(3.14*m_radius*m_radius);
}