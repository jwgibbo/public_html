#include <iostream>
#include <string>


int main()
{
	char symbol = '\0'; //single character
	int num = 0;
	std::string word = ""; //empty string
	
	
	symbol = 'A'; //single quotes!
	word = "A"; //double quotes!
	
	word = "banana";
	word = "oh no the wind is probably gonna to blow my house over. send help";
	
	
	//Goal: Get a word from the user
	std::cout << "Enter a word: ";
	std::cin >> word;
	
	std:: cout << "You entered: " << word << '\n';	
	
	//Do radical things!
	std::cout << "Length: " << word.length() << '\n';
	
	std::cout << "First character: " << word.at(0) << '\n';

	
	return(0);
}