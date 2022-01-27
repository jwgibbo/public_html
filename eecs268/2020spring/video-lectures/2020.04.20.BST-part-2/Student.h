
//Create a Student class in an attempt
//to model/abstraction of what a Student is

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
	//what data do student have?
	//What are the related data?	
	std::string m_name; 
	double m_gpa;
	std::string m_major;
	int m_id;
};

#endif