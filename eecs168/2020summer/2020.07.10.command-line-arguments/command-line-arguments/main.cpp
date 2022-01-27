#include <iostream>
#include <string>


int main(int argc, char** argv )
{	
	//Goal: If we have two arguments
	//assume the first is a word
	//and the second is a number
	//convert the number
	//print both
	//EXAMPLE: $>./prog dog 5
	std::string word="";
	int num=0;
	if(argc >= 3)
	{
		word = 	argv[1];
		num = std::stoi(argv[2]);
		std::cout << "Converting arguments...\n";
		std::cout << "The word is: " << word << '\n';
		std::cout << "The number is: " << num;
		std::cout << std::endl;
	}
	else
	{
		std::cout << "Not enough arguments!\n";
	}
	return(0);
}