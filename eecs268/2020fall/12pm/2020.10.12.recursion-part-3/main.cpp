#include <iostream>

int factorial(int n)
{
	if(n <= 1)
	{
		return(1);
	}
	else
	{
		return( n * factorial(n-1) );
	}
}


int main()
{
	int ans = 0;
	
	ans = factorial(2);
	
	std::cout << ans << '\n';
	
	return(0);
}