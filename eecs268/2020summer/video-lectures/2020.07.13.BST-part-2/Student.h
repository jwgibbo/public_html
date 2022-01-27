
#ifndef STUDENT_H
#define STUDENT_H

#include <string>

class Student
{
	public:
	Student(std::string name, double gpa, std::string major, int id);
	
	bool operator==(const Student& rhs) const;
	bool operator<(const Student& rhs) const;
	//overload > too, could be nice!

	bool operator==(int id) const;
	bool operator<(int id) const;
	//overload > too, could be nice!
	
	private:	
	std::string m_name; 
	double m_gpa;
	std::string m_major;
	int m_id;
};

#endif