//main.cpp
#include <iostream>

//Note: Quotes instead of <> around file 
#include "Student.h"

int main()
{
	int num = 5;
	Student myStu;//create a Student object
	Student myStu2;
	
	//myStu has all the components of a 
	//Student!
	myStu.name = "John Gibbons";
	myStu.id = 12345;
	myStu.major = "EECS";
	myStu.gpa = 2.5;
	
	myStu2.name = "Sara Connor";
	myStu2.id = 54321;
	myStu2.major = "BIO";
	myStu2.gpa = 4.0;
	
	std::cout << myStu.name << '\n';
	
	return(0);
}
