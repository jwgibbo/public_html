#include <iostream>

//Define a function named isEven
//it takes an int and returns a bool
//if the number is even, return true
//NOTE: a return type is a promise to
//		return a value of that type

//Define a function name myMax that takes two
//double and returns the larger of the two

//Define a function that takes a string and a
//a char and returns a count of how many that
//char was in the string 



//Goal: define a function that
// if given a number can calculate
// what 1 + that number is
int successor(int num)
{
	int answer = 0;
	answer = num + 1;
	return(answer);
}



int main()
{	
	int x = 5;
	int y = 0;
	
	y = successor(x);

	std::cout << "y=" << y << '\n';
	return(0);
}