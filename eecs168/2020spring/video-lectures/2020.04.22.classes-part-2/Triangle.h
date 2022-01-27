
//ifndef define block surround your header file code
//#ifndef FILE_NAME_H
#ifndef TRIANGLE_H
#define TRIANGLE_H

class Triangle
{
	public:
	//constructor
	//Constructor is special method with several 
	//rules: 
	//1) The name is the name of the class
	//2) No return type
	//3) Can only be called once per instace
	//4) Is automatically at the point where 	
	//		you allocate (i.e. declare) the object
	Triangle();
	
	//member variables
	double base;
	double height;
	
	//member methods 
	//(a method is a function that 
	//belongs to a class)
	double area(); //method declaration
	
};

#endif 