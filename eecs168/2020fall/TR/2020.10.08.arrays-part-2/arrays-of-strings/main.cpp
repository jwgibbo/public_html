#include <iostream>
#include <string>

int main()
{
	std::string* words = nullptr;
	int numWords = 0;
	
	std::string someString = "dog";
	
	std::cout << "How many words?: ";
	std::cin >> numWords;
	
	//create the array of strings
	words = new std::string[numWords];
	
	for(int i=0; i<numWords; i++)
	{
		std::cout << "Enter a word: ";
		std::cin >> words[i];
	}
	
	std::cout << "Here are the lengths of your words:\n";
	for(int i=0; i<numWords; i++)
	{
		std::cout << words[i].length() << '\n';
	}
	
	delete[] words;
	
	return(0);
}