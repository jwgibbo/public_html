#include <iostream>

int main()
{
	int x;
	
	std::cout << "Input a value for x: ";
	std::cin >> x;
	
	if( x > 0 )
	{
		std::cout << "x is positive\n";
	}
	else
	{
		std::cout << "x is NOT positive\n";	
	}
	
	std::cout << "Exiting..\n";
	return(0);
}