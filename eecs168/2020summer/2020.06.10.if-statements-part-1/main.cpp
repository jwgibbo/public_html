#include <iostream>

int main()
{
	int x = 0;
	std::cout << "Input a number: ";
	std::cin >> x;
	
	if ( x < 10 )
	{
	   std::cout << "x is small!\n";
	}
	else
	{
		std::cout << "x is at least 10\n";
		std::cout << "Way to go x!\n";
	}
	
	
	//code outside the if, runs no matter 
	//what. It runs unconditionally
	std::cout << "Goodbye!\n";
	return(0);
}

