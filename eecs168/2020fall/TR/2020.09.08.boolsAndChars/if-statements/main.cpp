#include <iostream>

int main()
{
	int userNum;
	
	std::cout << "Input a number: ";
	std::cin >> userNum;
	
	if(userNum > 0)
	{
		std::cout << "That's positive!\n";
	}
	else
	{
		std::cout << "That's not positive!\n";
	}
	
	return(0);
}