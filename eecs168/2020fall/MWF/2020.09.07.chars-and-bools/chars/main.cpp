#include <iostream>

int main()
{
	char symbol;
	
	//chars can be assigned to EXACTLY
	//one character.
	//chars use single quotes NOT " "
	symbol = '?';
	symbol = 'A';
	symbol = '5';
	symbol = 43;
	
	std::cout << "input a character: ";
	std::cin >> symbol;
	
	std::cout << "symbol = " << symbol << '\n';
	std::cout << "Goodbye...\n";
	return(0);
}