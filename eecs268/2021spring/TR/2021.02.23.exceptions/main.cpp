//main.cpp
#include <iostream>
#include <stdexcept>

int myDiv(int num, int denom)
{
	if( denom != 0 )
	{
		return( num/denom );
	}
	else
	{
		//Throw an exception
		throw(std::runtime_error("Division by zero"));
	}
}


int main()
{
	int ans = 0;
	
	ans = myDiv(10,2);
	std::cout << ans << '\n';
	
	ans = myDiv(0, 5); 
	std::cout << ans << '\n';

	try
	{	
		ans = myDiv(5, 0);
		std::cout << ans << '\n';
	}
	catch(std::runtime_error& rte)
	{
		std::cout << "Oops, you math broke. ";
		std::cout << "Here's why: ";
		std::cout << rte.what() << '\n';
	}
		
	std::cout << "Exiting gracefully...\n";
	
	return(0);
}











