#ifndef SHAPE_H
#define SHAPE_H

//NOTE: There won't be a Shape.cpp

class Shape
{
	public:
	//All methods will be pure virtual
	virtual double area() const = 0;
};

#endif