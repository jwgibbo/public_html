//Circle.h
#ifndef CIRCLE_H
#define CIRCLE_H

#include "Shape.h"

class Circle : public Shape
{
	private:
	double m_radius;
	
	public:
	Circle(double radius);
	double area() const;
};

#endif