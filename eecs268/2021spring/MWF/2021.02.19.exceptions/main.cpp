//main.cpp
#include <iostream>
#include <stdexcept>

int myDiv(int numerator, int denominator)
{
	if(denominator != 0)
	{
		return( numerator/denominator );
	}
	else
	{
		//We don't have a good value
		//to return
		throw(std::runtime_error("Division by zero."));
	}
}



int main()
{
	int ans = myDiv(10, 2);
	std::cout << ans << '\n';
	
	ans = myDiv(0,5);
	std::cout << ans << '\n';
	
	try
	{
		ans = myDiv(5, 0);
		std::cout << ans << '\n';
	}
	catch(std::runtime_error& rte)
	{
		//Handle the thrown 
		//exception
		std::cout << "Sorry, math broke. Here's why: ";
		std::cout << rte.what() << '\n';
	}
	
	std::cout << "Exiting gracefully...\n";
	return(0);
}





