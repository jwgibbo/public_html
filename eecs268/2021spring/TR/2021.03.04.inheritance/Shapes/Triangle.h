#ifndef TRIANGLE_H
#define TRIANGLE_H

#include "Shape.h"

class Triangle : public Shape
{
	public:
	Triangle(double base, double height);
	
	//MUST be defined!
	double area() const;
	
	protected:
	double m_base;
	double m_height;
	
};

#endif