//Triangle.h

//Add a compiler macro to let the compiler
//know if already has this class to not
//add it a second time
#ifndef TRIANGLE_H
#define TRIANGLE_H

class Triangle
{
	private:
	//member variables
	double base;
	double height;
	
	public:
	//member methods
	double getBase();
	double getHeight();
	bool setBase(double newBase);
	//bool setHeight(double newHeight);
};

#endif