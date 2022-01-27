//Circle.h
#ifndef CIRCLE_H
#define CIRCLE_H

#include "Shape.h" 
class Circle : public Shape
{
	public:
	Circle(double radius);
	double circumference() const;
	double area() const;
	
	private:
	double m_radius;
};


#endif