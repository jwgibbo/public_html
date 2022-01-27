#ifndef SHAPE_H
#define SHAPE_H

class Shape
{
	public:
	//Pure virtual method
	//The = 0 is not a return it means
	//there is no definition
	virtual double area() const = 0;
};

#endif