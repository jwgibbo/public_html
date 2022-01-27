//Course.h

#ifndef COURSE_H
#define COURSE_H

#include <string>

class Course
{
	public:
	Course( std::string dept, int number );
	~Course();
	
	std::string getDept() const;
	int getNumber() const;
	
	//Define the overloading of ==
	bool operator==(const Course& rhs) const;
	
	//Copies all the ids into the course's array
	bool enroll(int* roster, int numStudents);
	
	private:
	//A convention I use, is optional
	std::string m_dept;
	int m_number;
	int* m_ids; //Array of ids
	int m_numEnrolled; //Size of the array
	
};

#endif