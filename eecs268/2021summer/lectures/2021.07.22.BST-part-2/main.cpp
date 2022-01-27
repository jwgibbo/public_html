

#include "BST.h"
#include "Student.h"

int main()
{
	BST<Student, int> myRoster;
	Student stu1("Billy", 2.5, 412);
	Student temp;
	
	myRoster.add(stu1);
	
	temp = myRoster.search(412);//return Billy
}