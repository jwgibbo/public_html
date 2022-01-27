#include <iostream>

int main()
{
	//Goal: Prompt the user over and
	//over until they provide a positive
	//integer	
	
	int userNum = 0;
	
	do
	{
		std::cout << "Input a value: ";
		std::cin >> userNum;
	}while( userNum <= 0 );
	
	std::cout << "Your positive value: ";
	std::cout << userNum << '\n';
	std::cout << "Thanks! Goodbye!\n";
	
	return(0);
}

