#include <iostream>

int main()
{
	//Goal: Create a guessing game for the user.
	//To exit, they must guess the number 10
	
	const int SECRET_NUM = 10;
	int userGuess = 0;

	do
	{
		std::cout << "Input a guess: ";
		std::cin >> userGuess;
	}while( userGuess != SECRET_NUM );
	
	std::cout << "You win!\n";
	
	return(0);
}
