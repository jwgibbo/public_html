#include "Student.h"


Student::Student(std::string name, double gpa, std::string major, int id)
{
	m_name = name;
	m_gpa = gpa;
	m_major = major;
	m_id = id;
}


bool Student::operator==(const Student& rhs) const
{
	//if they ids are the same, they're the same student
	return(m_id == rhs.m_id);
}

bool Student::operator==(int id) const
{
	return(m_id == id);
}

bool Student::operator<(int id) const
{
	return(m_id < id);
}