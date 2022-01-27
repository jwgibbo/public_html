//ifndef define block surround your header file code
//#ifndef FILE_NAME_H
#ifndef TRIANGLE_H
#define TRIANGLE_H

class Triangle
{
	private:
	//member variables
	double m_base;
	double m_height;
	
	public:
	Triangle();
	double area(); //method declaration
	double getBase();
	double getHeight();
	
	bool setBase(double base);
	bool setHeight(double height);
};

#endif 