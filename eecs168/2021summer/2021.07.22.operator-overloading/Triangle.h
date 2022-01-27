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
	//Triangle();
	Triangle(double newBase, double newHeight);
	
	//member methods
	bool operator>(const Triangle& rhs) const;
	bool operator<=(const Triangle& rhs) const;
	double getBase() const;
	double getHeight() const;
	bool setBase(double newBase);
	bool setHeight(double newHeight);
	double area() const;
};

#endif