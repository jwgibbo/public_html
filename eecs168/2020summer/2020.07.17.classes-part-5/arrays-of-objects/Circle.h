//header file for Circle class
//header file is where the class definition
#ifndef CIRCLE_H
#define CIRCLE_H

class Circle
{
	//Private members are ONLY directly
	//accessible inside of the class header and 
	//implementation files
	private:
	
		//member variables
		double m_radius;
	
	public:	
		//Constructor
		Circle();
		Circle(double radius);
		
		//member methods
		//FYI methods are just functions 
		//that belong to classes
		double area() const;
		
		//getter and setter for the radius
		bool setRadius(double radius);
		
		double getRadius() const;
};


#endif