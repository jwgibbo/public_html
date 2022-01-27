#include <iostream>
#include <string>

//for local files, use "" instead of <>
#include "Student.h"

int main()
{	
	//Declare a Student object
	//AKA declare an instance of the Student class
	Student myStudent;
	Student otherStudent;
		
	myStudent.name = "John Gibbons";
	myStudent.id = 12345;
	myStudent.gpa = 2.8;
	myStudent.major = "EECS";
	
	otherStudent.name = "Molly Fibbons";
	otherStudent.id = 54321;
	otherStudent.gpa = 4.0;
	otherStudent.major = "MATH";
	return(0);
}