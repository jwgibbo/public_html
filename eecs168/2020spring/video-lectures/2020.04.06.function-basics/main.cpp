#include <iostream>
#include <math.h>

/* Function definition template:

returnType functionName( optional parameter list )
{
	body of the functionName
	what does this function do?
	
	return( value or variable );
}


*/

/*BOARD WORK:
1) define a function that takes an int and
	returns true is that number is even.
	return false otherwise.
2) define a function that takes two ints and
	returns the sum of all values from the first to 
	the second(inclusively). Assume good parameters.
3) define a function that takes a std::string and a 
	character. It return the number of times that char
	occurs in the string 
*/

/*
bool isEven(int num)
{
	//function body
}
*/

//Function definition
int successor(int num)
{
	int ans = num + 1;
	std::cout << "Function called!\n";
	return(ans);
}

int main()
{
	double ans  = 0;
	int test = 0;
	ans = sqrt(9.5); //calling sqrt
	
	test = successor(5);
	std::cout << "test = " << test << '\n';
	std::cout << ans << '\n';
	
	return(0);
}
