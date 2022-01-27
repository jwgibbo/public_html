#include <iostream>
//This is a comment. Comments are ignored by the 
//compiler.

//Remember to put a semicolon at the end of each cout!

/* This is a multiline comment. It's starts with
	a forward-slash and asterix and can span as
	many lines as you need. It is concluded with a 
	asterix and a forward slash
*/
int main()
{
	std::cout << "Hello, World!";
	std::cout << std::endl;
	std::cout << "Goodbye Mars!\n";
	std::cout << "Todo list:\n";
	std::cout << "\tLearn special characters\n";
	std::cout << "\tPrint math\n";
	std::cout << "\tPrint multiples things\n";
	
	std::cout << ((42+1)*7);
	std::cout << "\n";
	
	std::cout << "(7*15) = " << (7*15) << std::endl;
	
	return (0);
}

/*BOARD WORK!
	Create a main.cpp that can tell the user
	how you will be in the year 36354
	(Use math!)
*/