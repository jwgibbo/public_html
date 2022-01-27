#include <iostream>

int main()
{
	//GOAL: Make the user gues the value
	//      33 
	const int SECRET_NUM = 33;
	int userGuess = 0;
	
	do
	{
		std::cout << "Enter a guess: ";
		std::cin >> userGuess;
	}while( userGuess != SECRET_NUM );
	
	std::cout << "You win!\n";
	return(0);
}