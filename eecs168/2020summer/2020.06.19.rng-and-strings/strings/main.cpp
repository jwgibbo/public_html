#include <iostream>
#include <string>

int main()
{	
	//int num = 0;
	
	//declare a string:
	std::string myWord = "";//empty string
	std::string userWord = "";
	
	/* String notes:
	-hold zero or more characters
	-always use double quotes (") to surround them
	*/
	
	//assign string some values:
	myWord = "abc";
	myWord = "123";
	myWord = "ksdhakljfhaklfhkhkh";
	myWord = "John Gibbons!";
	
	std::cout << "Input a word: ";
	std::cin >> userWord;
	
	std::cout << "You typed: " << userWord;
	std::cout << std::endl;
	
	std::cout << "That has " << userWord.length();
	std::cout << " characters\n";
	
	//print the first character:
	std::cout << "First character: " << userWord.at(0) << '\n';
	
	//print the last character
	std::cout << "Last character: " << userWord.at(userWord.length()-1) << '\n';
	
	//print every character on its own line:
	for(unsigned int i=0; i<=userWord.length()-1; i++)
	{
		std::cout << userWord.at(i) << '\n';
	}
	
	
	return(0);
}