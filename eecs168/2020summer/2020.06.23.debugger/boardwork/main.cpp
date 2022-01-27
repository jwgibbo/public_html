#include <iostream>
#include <time.h>
#include <stdlib.h>

int main()
{	
	int secretNum=0;
	int userGuess=0;
	
	srand(time(NULL));
	
	do
	{
		secretNum = (rand()%10)+1;
		
		std::cout << "What's your guess: ";
		std::cin >> userGuess;		
				
	}while(userGuess != secretNum);
	
	std::cout << "You guessed it!\n";
	
	return(0);
}