//main.cpp
#include <iostream>
#include "Student.h"//NOTE: "" not <>

int main()
{
	Student myStudent;
	Student yourStudent;
	
	//Assign the student values
	myStudent.name = "Joe";
	myStudent.id = 1234;
	myStudent.gpa = 2.9;
	
	yourStudent.name = "Jan";
	yourStudent.id = 1235;
	yourStudent.gpa = 4.0;
	
	std::cout << myStudent.name << '\n';
	std::cout << myStudent.id << '\n';
	std::cout << myStudent.gpa << '\n';
	return(0);
}