#include <iostream>

void byValueFunc(int n)
{
	std::cout << "Hahaha!\n";
	n = 99;
}

void byRefFunc(int& n)
{
	std::cout << "Hahaha!\n";
	n = 99;
}


int main()
{
	int num = 5;

	std::cout << num << '\n';
	num = byValueFunc(42);
	std::cout << num << '\n';
	//byRefFunc(42); ERROR
	std::cout << num << '\n';
	return(0);
}