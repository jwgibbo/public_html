#include <iostream>

int main()
{
	//Goal: Ask the user for a number
	//		until they type in 4
	
	int userGuess = 0;
	const int SECRET_NUM = 4;
	
	do
	{
		std::cout << "Guess a number: ";
		std::cin >> userGuess;
	}while(userGuess != SECRET_NUM);
	
	return(0);
}