#include <iostream>

int main()
{
	//Prompt the user for a number 
	//over and over until they type in 55
	
	
	int userNum = 0;
	
	std::cout << "Input a number: ";
	std::cin >> userNum;
	
	while ( userNum != 55 )
	{
		std::cout << "Input a number: ";
		std::cin >> userNum;
	}		
	
	return(0);
}