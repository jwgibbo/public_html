//main.cpp
#include <iostream>
#include "Course.h"

int main()
{
	Course myCourse("EECS", 168);
	Course yourCourse("MATH", 125);
	
	//Create an array ids
	const int SIZE = 3;
	int stuIDs[SIZE];
	stuIDs[0] = 12345;
	stuIDs[1] = 54321;
	stuIDs[2] = 98765;
	
	//enroll them in EECS 168;
	myCourse.enroll(stuIDs, SIZE);
	
	std::cout << myCourse.getDept() << ' ';
	std::cout << myCourse.getNumber() << '\n';
	
	//We need to overload this operator
	if( myCourse == yourCourse )
	{
		std::cout << "Same course!\n";
	}
	else
	{
		std::cout << "Not the same course!\n";
	}
	
	
	return(0);
}









