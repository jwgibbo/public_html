//Triangle.cpp

#include "Triangle.h"

Triangle::Triangle(double base, double height)
{
	m_base = base;
	m_height = height;
}

double Triangle::area() const
{
	//area = (1/2) * base * height
	return(0.5*m_base*m_height);
}