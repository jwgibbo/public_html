#include <iostream>
#include <string>

//Define a function that takes two doubles by reference
//and swaps their values

//Define the following function...
void checkerBoard(int n, char symbol1, char symbol2)
{
	//prints an nxn checkerboard pattern 
	//of alternating symbols
}



//Define a function that takes a name
//and prints: "Hello <name>!"
void greeting(std::string name)
{
	std::cout << "Hello, " << name << "!\n";
	return;//just ends the function
}


//Goal: Define a function that takes
//an int and assigns it to -1
void changer(int& num)
{
	num = -1;
	return;
}

//Goal: define a function that
// if given a number can calculate
// what 1 + that number is
int successor(int num)
{
	int answer = 0;
	answer = num + 1;
	num = 99;//does NOT change main's variable
	return(answer);
}


int main()
{	
	int x = 5;
	
	changer(x);
	std::cout << "x = " << x << '\n';
	return(0);
}