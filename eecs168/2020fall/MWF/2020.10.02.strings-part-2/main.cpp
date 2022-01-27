#include <iostream>
#include <string>
#include <limits>

int main()
{
	std::string phrase = "";
	int num = 0;
	
	std::cout << "Enter a number: ";
	std::cin >> num;
	std::cout << "num = " << num << '\n';
	
	//when switching from std::cin to 
	//getline, flush the buffer
	//Don't forget to include limits library
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	
	std::cout << "Input a phrase: ";
	//get a line of input up to but not
	//including a newline character. Then
	//throw out the trailing newline.
	//Input is taken from terminal (cin)
	//and stored in phrase (our string)
	std::getline(std::cin, phrase);
	std::cout << phrase << '\n';
	
	std::cout << "Input another phrase: ";
	std::getline(std::cin, phrase);
	std::cout << phrase << '\n';
	
	return(0);
}