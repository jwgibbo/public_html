#include <iostream>

//Include the local file, Student.h
#include "Student.h"

int main()
{
	//Declare an instance of the Student
	//class...dut dut duuuuuun!
	Student myStu; //no intial value needed
	Student myStu2;
	
	
	//Access the public members
	myStu.name = "John";
	myStu.id = 1234567;
	myStu.gpa = 2.5;
	myStu.major = "EECS";
	
	myStu2.name = "Susie";
	myStu2.id = 7654321;
	myStu2.gpa = 4.0;
	myStu2.major = "EECS";
	
	return(0);
}



