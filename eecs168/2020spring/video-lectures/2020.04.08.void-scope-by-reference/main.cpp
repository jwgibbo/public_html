#include <iostream>
#include <string>
#include <math.h>
//This function does work
//but doesn't hand back a value
//Unlike functions that return values
//void function cannot be used any place
//you need a value (e.g. cout, assignment)
void greeting(std::string name)
{
	std::cout << "Hi " << name << "!\n";
	return;//No value returned
	std::cout << "Goodbye " << name << "!\n";
}

//Function definition
int successor(int num)
{
	int ans = num + 1;
	return(ans);
}

int previous(int num)
{
	int ans = num - 1;
	return(ans);
}

void numChanger(int& num)
{
	num = 99;
	std::cout << "muahahahaha!\n";
	return;
}

int main()
{
	double ans  = 0;
	int test = 0;
	std::string str="";
	test = successor(54); //calling successor
	
	numChanger(test);//test will be ???
	std::cout << "test = " << test << "\n";

	return(0);
}

/* BOARD WORK

1) Create a void function that takes a string and 
	number and prints the string num times each 
	on it's own line
	
2) Create a void function that takes an int n, which
	represents the n for an nXn grid of the following
	pattern:
	(assume n=5)
	ababa
	babab
	ababa
	babab
	ababa
	
3) Create a swap function that takes two double
	variables and exchanges their values. 
	
4) Create a function that takes two strings and
	returns true only if they are the same length
	and have the same characters in the same order
	(case-sensitive).
*/