#include <iostream>
#include <string>

int main()
{
	std::string word = "dog"; //single string object
	std::string* words = nullptr; //string pointer
	int numWords = 0;
	
	std::cout << "How many words will your write?: ";
	std::cin >> numWords;
	
	//create the array of string objects
	words = new std::string[numWords];
	
	for(int i=0; i<numWords; i++)
	{
		std::cout << "Enter a word: ";
		std::cin >> words[i];
	}
	
	for(int i=0; i<numWords; i++)
	{
		std::cout << words[i] << " which is ";
		std::cout << words[i].length() << '\n';
	}
	
	//alter this code to print each letter of each word
	//on it's own line. HINT: nested loop
	
	
	
	delete[] words;
	return(0);
}