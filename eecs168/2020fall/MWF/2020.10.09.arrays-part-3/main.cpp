#include <iostream>
#include <string>

int main()
{
	int numWords = 0;
	std::string* words = nullptr;
	
	std::cout << "How many words?: ";
	std::cin >> numWords;
	
	words = new std::string[numWords];
	
	for(int i=0; i<numWords; i++)
	{
		std::cout << "Enter a words: ";
		std::cin >> words[i];
	}
	
	std::cout << "Here are your lengths:\n";
	for(int i=0; i<numWords; i++)
	{
		std::cout << words[i].length() << '\n';
	}
	
	delete[] words;
	return(0);
}