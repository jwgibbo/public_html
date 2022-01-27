#ifndef SHAPE_H
#define SHAPE_H

class Shape
{
	public:
	//area is a pure virtual method.
	//It has no definition.
	//The derived types MUST define area
	virtual double area() const = 0;
};

#endif