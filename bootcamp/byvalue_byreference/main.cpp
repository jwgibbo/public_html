#include <iostream>

void byValueFunc(int n)
{
	std::cout << "Hahaha!\n";
	n = 99;
}

void byRefFunc(int& n) //NOTE the &
{
	std::cout << "Hahaha!\n";
	42 = 99;
}

int main()
{
	int num = 5;
	std::cout << num << '\n';

	byValueFunc(num);
	std::cout << num << '\n';
	byRefFunc(num); 
	std::cout << num << '\n';

	byValueFunc(42);
	// byRefFunc(42);  ERROR
	return(0);
}
