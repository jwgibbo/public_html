#include <iostream>
#include <string>

int main()
{
	std::string phrase = "\"";
	
	std::cout << "Input a string: ";
	std::cin >> phrase;
	
	if(phrase.at(0) == 'b')
	{
		std::cout << "First letter is b\n";
	}
	
	return(0);
}