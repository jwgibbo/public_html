//Circle.h

//Compiler macro to allow for multiple
//includes of this file
//You'll do this in all your .h files
#ifndef CIRCLE_H
#define CIRCLE_H

class Circle
{
	public:
	//member variable
	double radius;
	
	//member method
	//FYI, method just means a function
	//that belongs to a class
	double area();
	
};

#endif