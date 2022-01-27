#include <iostream>

int main()
{
	int userAge;
	
	std::cout << "How old are you?: ";
	std::cin >> userAge;
	
	std::cout << "Wow! You're " << userAge << " years old!\n";
	
	return(0);
}