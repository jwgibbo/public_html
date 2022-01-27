#include <iostream>

int main()
{
	//char is a new data type for 
	//storing characters
	
	//backslash zero is null character
	char symbol = '\0';
	
	std::cout << "What does the null character look like? :" << symbol << "interesting!\n";
	
	//assign to a character, but
	//it must be exactly one character
	//surrounded by single quotes
	
	//quick examples of valid chars
	symbol = '$';
	symbol = '!';
	symbol = 'A';
	symbol = '5'; //the character five
	symbol = ' ';
	symbol = '\n';//the newline character
	symbol = '\t';//the tab character
	
	//character can cin-ed and cout-ed 
	//just like other data types
	std::cout << "what's your first initial?: ";
	std::cin >> symbol;
	
	std::cout << "Your first initial is: ";
	std::cout << symbol << "\n";
	
	return(0);
}

