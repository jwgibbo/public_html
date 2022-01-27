#include <iostream>
//Note " " instead of < >
#include "Student.h"

/* 
1) Create a Triangle.h 
-Triangle have a base and a height (e.g. 10.5 and 7.2)

2) In main.cpp
-Ask the user for the base and height of two different 
	Triangles
-Print the base and height of the Triangle with the larger
	area. (reminder (1.0/2.0) * base * height)
*/


int main()
{
	int x = 0;

	//Declare an instance of the Student class
	Student myStudent; //no initialization...yet
	Student stu2; 
	
	//Assign the Student a name
	myStudent.name = "John";
	myStudent.major = "EECS";
	myStudent.gpa = 3.8;
	myStudent.id = 1234567;
	
	stu2.name = "Zanthabar";
	stu2.major = "MATH";
	stu2.gpa = 4.00;
	stu2.id = 1000000;
	
	//print the student's name and major
	std::cout << "Name: " << myStudent.name <<'\n';
	std::cout << "Major: " << myStudent.major << '\n';
	
	std::cout << "Name: " << stu2.name << '\n';
	std::cout << "Major: " << stu2.major << '\n';
	return(0);
}