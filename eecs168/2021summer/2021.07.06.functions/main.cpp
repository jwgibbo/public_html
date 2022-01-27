#include <iostream>

int nextNum(int num);

int main()
{
	int after5 = 0;
	
	after5 = nextNum(5);
	
	std::cout << after5 << '\n';
	std::cout << nextNum(99) << '\n';
	return(0);
}

//Goal: Define a function that takes a whole number
//		and returns the next number in sequence
//		Example: this function called with 5 as
//		the parameter, it return 6
int nextNum(int num)
{
	int ans = 0; //ans is just a variable name
	ans = num + 1;
	return( ans );
}