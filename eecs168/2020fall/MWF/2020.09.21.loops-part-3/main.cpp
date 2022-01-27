#include <iostream>

int main()
{
	//Ask the user for a number over and 
	//over until they enter 55
	int userNum = 0;
	
	std::cout << "Enter a value: ";
	std::cin >> userNum;
	
	while ( userNum != 55 )
	{
		std::cout << "Enter a value: ";
		std::cin >> userNum;		
	}
	
	return(0);
}