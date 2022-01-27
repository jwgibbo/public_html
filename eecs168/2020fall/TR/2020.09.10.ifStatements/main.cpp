#include <iostream>

int main()
{
	//declares and initializes score
	double score = 0;
	
	std::cout << "Input a score: ";
	std::cin >> score;
	
	if( score >= 90 )
	{
		std::cout << "You got an A!\n";
	}
	else
	{
		std::cout << "You got a B!\n";
	}
	
	
	return(0);
}