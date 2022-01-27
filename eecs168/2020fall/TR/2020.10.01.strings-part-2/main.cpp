#include <iostream>
#include <string>
#include <limits>

int main()
{
	std::string word1 = ""; //empty string
	std::string word2 = "";
	std::string line = "";
	int num = 0;
	
	std::cout << "input a number: ";
	std::cin >> num;
	std::cout << "num = " << num << '\n';
	
	//Flush the input stream
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	
	std::cout << "Enter a phrase: ";
	std::getline(std::cin, line);
	std::cout << line<< '\n';
	
	return(0);
}