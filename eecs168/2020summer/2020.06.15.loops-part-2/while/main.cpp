#include <iostream>

int main()
{
	
	//Goal: Prompt the user over and
	//over until they provide a positive
	//integer	

	int userNum = 0;
	
	std::cout << "Input a value: ";
	std::cin >> userNum;
	
	while ( userNum <= 0 )
	{
		//Get another value
		std::cout << "Input a value: ";
		std::cin >> userNum;
	}

	std::cout << "Your positive value: ";
	std::cout << userNum << '\n';
	std::cout << "Thanks! Goodbye!\n";

	return(0);
}

