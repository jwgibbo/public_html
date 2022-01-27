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
	//other methods can still be added
	//but aren't required or accessible
	//through the interface
};

#endif