#include <iostream>

//Precondition: n>=1
int factorial(int n)
{
	//base case
	if( n <= 1 )
	{
		return( 1 );
	}
	//recursive case
	else
	{
		return(n*factorial(n-1));
	}
}

int main()
{	
	int ans = 0;
	
	ans = factorial(16); //initial call
	
	std::cout << "factorial: " << ans << '\n';
	return(0);
}