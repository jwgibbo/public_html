#include <iostream>

int main()
{
	char symbol;
	
	//characters are EXACTLY one
	//symbol surrounded by single quotes
	//NOT double quote
	symbol = 'A';
	symbol = '?';
	symbol = '5';//Not the number 5
	symbol = ' ';
	symbol = '\n';
	symbol = 99;
	std::cout << "symbol = " << symbol;
	std::cout << std::endl;
	return(0);
}