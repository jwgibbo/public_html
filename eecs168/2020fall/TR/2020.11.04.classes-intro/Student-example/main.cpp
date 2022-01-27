#include <iostream>
#include "Student.h"

int main()
{
	Student myStu; //No initialzation...yet
	Student stuTwo;
	
	//Assign values to its public member
	//variable
	myStu.name = "John";
	myStu.id = 12345;
	myStu.gpa = 2.0;
	myStu.major = "EECS";
	
	stuTwo.name = "Susie";
	stuTwo.id = 54321;
	stuTwo.gpa = 4.0;
	stuTwo.major = "EECS";
	
	return(0);
}
