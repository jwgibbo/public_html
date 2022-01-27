#include <iostream>

int main()
{
	//Declare a variable
	int userNum = 0;
	int twiceUserNum = 0;

	//Ask the user user for a value
	std::cout << "Input a number: ";
	std::cin >> userNum;
	
	//Calculate twice the user's number
	twiceUserNum = 2*userNum;
	
	std::cout << "userNum = " << userNum << std::endl;
	std::cout << "twiceUserNum = " << twiceUserNum << std::endl;
	return(0);
}