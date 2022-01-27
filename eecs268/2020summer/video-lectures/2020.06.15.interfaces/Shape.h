#ifndef SHAPE_H
#define SHAPE_H

class Shape
{
	public:
	//list a required method for all
	//Shapes, but not provide the 
	//definition.
	//Force the derived classes to provide
	//the definition
	//Pure virtual definition: method
	//without a definition
	virtual double area() const = 0;
	
	
	//no member variables
	//no constructor 
};

#endif