#include <iostream>

int main()
{
	//Goal: Ask the user for a number
	//		Do not stop getting numbers
	//		from the user until they type
	//		the number 4
	
	const int SECRET_NUM = 4;
	int userGuess = 0;
	
	std::cout << "Guess the secret number: ";
	std::cin >> userGuess;
	
	while( userGuess != SECRET_NUM )
	{
		std::cout << "Sorry, guess again: ";
		std::cin >> userGuess;
	}
		
	return(0);
}