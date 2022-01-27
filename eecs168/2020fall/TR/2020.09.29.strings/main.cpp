#include <iostream>
#include <string>


int main()
{
	std::string word1 = ""; //empty string
	std::string word2 = "";
	
	std::cout << "input a two words: ";
	std::cin >> word1;
	std::cin >> word2;
	
	std::cout << word1 << '\n';
	std::cout << word2 << '\n';

	return(0);
}