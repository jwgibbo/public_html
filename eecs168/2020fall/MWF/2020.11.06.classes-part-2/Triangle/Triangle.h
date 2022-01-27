//Triangle.h

//Wrap the header file with note to the compile
//that tells it to only include the definition once
//This avoid redefinition errors
#ifndef TRIANGLE_H
#define TRIANGLE_H

class Triangle
{
	public:
	
	//member varables
	double base;
	double height;
	
	//member methods
	//NOTE: methods are just functions that belong
	//to a class
	double area();
	
};
#endif