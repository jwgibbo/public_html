#include <iostream>

int main()
{
	char symbol = '\0';
	char letter1 = '\0';
	char letter2 = '\0';
	char letter3 = '\0';
	
	symbol = 'a';
	std::cout << "symbol = " << symbol << ".\n";
	
	symbol = 'R';
	std::cout << "symbol = " << symbol << ".\n";
	
	symbol = '?';
	std::cout << "symbol = " << symbol << ".\n";
	
	symbol = '\n';
	std::cout << "symbol = " << symbol << ".\n";

	symbol = '5';//character 5 NOT number 5
	std::cout << "symbol = " << symbol << ".\n";

	symbol = ' ';
	std::cout << "symbol = " << symbol << ".\n";

	std::cout << "Input 3 letters: ";
	std::cin >> letter1 >> letter2 >> letter3;
	std::cout << "letter1 = " << letter1 << "\n";
	std::cout << "letter2 = " << letter2 << "\n";
	std::cout << "letter3 = " << letter3 << "\n";
	return(0);
}