#include <iostream>

int main()
{
	double userScore = 0;
	
	std::cout << "Input a score: ";
	std::cin >> userScore;
	
	if( userScore >= 90 )
	{
		std::cout << "You got an A\n";
	}
	else if( userScore >= 80 )
	{
		std::cout << "You got a B\n";
	}
	
	
	return(0);
}