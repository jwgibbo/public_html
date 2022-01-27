#include <iostream>

int main()
{
	int userNum = 0;
	
	std::cout << "Input a number: ";
	std::cin >> userNum;
	
	if(userNum > 0)
	{
		std::cout << "It's positive!\n";
	}
	else
	{
		std::cout << "It's not positive!\n";
	}	
	
	return(0);
}