#include <iostream>

void byReferenceFunc(int& n)
{
	std::cout << "Hahaha!\n";
	n = 99;
	std::cout << "n = " << n << '\n';
}


void byValueFunc(int n)
{
	std::cout << "Hahaha!\n";
	n = 99;
	std::cout << "n = " << n << '\n';
}


int main()
{
	int num = 5;
	
	byValueFunc(5);
	std::cout << "num = " << num << '\n';

	byReferenceFunc(num);
	
	std::cout << "num = " << num << '\n';

	return(0);
}



