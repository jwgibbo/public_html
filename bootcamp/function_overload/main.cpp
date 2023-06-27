//main.cpp
//function overloading demo
#include <iostream>

void funky_town(int n)
{
	std::cout << "An int is in funky town!" << std::endl;
}

void funky_town(double n)
{
	std::cout << "A double is in funky town!" << std::endl;
}

void funky_town(std::string n)
{
	std::cout << "A string is in funky town!" << std::endl;
}

void funky_town(int i, double d)
{
	std::cout << "An int and double are in funky town!" << std::endl;
}

int main()
{
	funky_town(55);
	funky_town(0.5);
	funky_town("55");
	funky_town(55, 3.14);
	return (0);
}
