#include <iostream>
#include <string>

int main()
{
	std::string phrase = "";//empty string		
	
	phrase = "I love bananas";
	std::cout << phrase << '\n';
	
	phrase = "1234";
	std::cout << phrase << '\n';
	
	phrase = "John Gibbons\n";
	std::cout << phrase << '\n';
	
	std::cout << "Input a phrase: ";
	std::cin >> phrase;
	
	std::cout << "Here is your phrase:\n";
	std::cout << phrase << '\n';
	
	std::cout << "Your phrase is ";
	std::cout << phrase.length();
	std::cout << " characters long.\n";
	
	//Goal: Print all the letters in the phrase
	//		each on its own line
	for(unsigned int i=0; i<phrase.length(); i++)
	{
		std::cout << phrase.at(i) << '\n';
	}
	
	return(0);
}