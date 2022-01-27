#ifndef TRIANGLE_H
#define TRIANGLE_H

#include "Shape.h"

class Triangle : public Shape
{
	private:
	double m_base;
	double m_height;
	
	public:
	Triangle(double base, double height);
	double area() const;
	//other methods can still be added
	//but aren't required or accessible
	//through the interface
};

#endif