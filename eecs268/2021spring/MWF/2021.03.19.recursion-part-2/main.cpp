#include <iostream>

//Precondition: n>=0
int factorial(int n)
{
	//base case
	if( n == 1 || n == 0)
	{
		return(1);
	}
	else if( n > 1)
	{
		return(n*factorial(n-1));
	}
	else
	{
		throw(std::runtime_error("Bad n passed to factorial"));
	}
}


int main()
{	
	std::cout << factorial(-5) << '\n';
	
	return(0);
}