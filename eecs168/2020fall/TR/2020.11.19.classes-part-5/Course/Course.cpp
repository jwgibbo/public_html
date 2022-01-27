//Course.cpp

#include "Course.h"

Course::Course(std::string dept, int number)
{
	if( dept.length() == 3 || dept.length() == 4)
	{
		m_dept = dept;
	}
	else
	{
		//We don't have a great option
		//to deal with bad paramters in
		//constructors
		m_dept = "ERROR";
	}
	
	if( number > 0 && number <= 999 )
	{
		m_number = number;
	}
	else
	{
		m_number = 0;
	}
	
	m_ids = nullptr;
	m_numEnrolled = 0;
}

Course::~Course()
{
	//We just need to clean up anything we put
	//on the heap
	if( m_ids != nullptr )
	{
		delete[] m_ids;
	}
	
}

std::string Course::getDept() const
{
	return( m_dept );
}

int Course::getNumber() const
{
	return( m_number );
}

bool Course::operator==(const Course& rhs) const
{
	return( m_dept == rhs.m_dept && m_number == rhs.m_number );
}



bool Course::enroll(int* roster, int numStudents)
{
	if( m_ids == nullptr )
	{
		//make a copy of the roster
		m_ids = new int[numStudents];
		
		for(int i=0; i<numStudents; i++)
		{
			m_ids[i] = roster[i];
		}
		
		//save the size!
		m_numEnrolled = numStudents;
		return (true);	
	}	
	else
	{
		return (false);
	}
}







