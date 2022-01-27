#include <iostream>
//Note " " instead of < >
#include "Student.h"

int main()
{
	Student stu1("Bob", 3.0, "EECS", 12345);
	Student stu2("Susy", 3.5, "EECS", 54321);
	std::string str1 = "dog";
	std::string str2 = "banana";
	
	std::cout << str2.length() << '\n';
	
	/* calls my operator== method
		stu1 is the calling object
		stu2 is the parameter (rhs)
	*/
	if( stu1 == stu2 )
	{
		std::cout << "Same student!\n";
	}
	else
	{
		std::cout << "Not the same student\n";
	}
	
	/*Compare a student object to an id*/
	if(stu2 == 54321)
	{
		std::cout << "Match!\n";
	}
	else
	{
		std::cout << "No Match!\n";
	}
	
	/*YOU CANNOT DO THE FOLLOWING:
	if(54321 == stu2)
	{
		std::cout << "Match!\n";
	}
	else
	{
		std::cout << "No Match!\n";
	}
	*/
	return(0);
}