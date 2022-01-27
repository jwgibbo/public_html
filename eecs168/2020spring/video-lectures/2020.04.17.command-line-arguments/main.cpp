#include <iostream>
#include <string>

//argc count of the arguments
//argv 2D character array
//Each array is a null terminated array
int main(int argc, char** argv)
{
	//goal check to make sure the user passed in
	//two command line arguements (not counting
	//the program's name.
	//If they passed two arguements print them
	//convert them to ints and add them together.
	//Otherwise, print an error message and exit
	//gracefully.
	std::string arg1="";
	std::string arg2="";
	double num1=0;
	double num2=0;
	
	if(argc == 3)
	{
		//string = char* works!
		arg1 = argv[1];
		arg2 = argv[2];
		
		//convert a string to an int
		num1 = std::stod(arg1);
		num2 = std::stod(arg2);
		
		std::cout << "Your arguments were:\n";
		std::cout << num1 << '\n' << num2 << '\n';
		std::cout << "Sum: " << (num1+num2) <<'\n';
	}
	else
	{
		std::cout << "Incorrect number of arguments\n";
		std::cout << "Exiting...\n";
	}
	
	return(0);
}

/* BOARD WORK
In a fresh main that requires the user to pass in
two words. If they don't pass in two words, print an
error message and exit. Otherwise print the longer
of the two words to the user and ask them for a 
character to count. Then print a count of how many
times that character is in the longer word.

Example:

$>./prog cat banana
Longer word: banana
What character do you want to count?: a
Count: 3

default to choosing first in case of tie
$>./prog aaaaaa banana
Longer word: aaaaaa
What character do you want to count?: a
Count: 6

$>./prog cat banana
Longer word: banana
What character do you want to count?: z
Count: 0
*/