//main.cpp
#include "CoolString.h"
#include <iostream>
#include <stdexcept>

int myDiv(int num, int denom)
{
	if( denom != 0 )
	{
		return( num / denom );
	}
	else
	{
		throw (std::runtime_error("ERROR: Division by zero!\n"));
	}	
}


int main()	
{
	int ans = 0;
	
	try
	{
		ans = myDiv(10, 5);
		std::cout << "ans = " << ans << '\n';
	}
	catch (std::exception& e)
	{
		//handle the exception
		std::cout << "Something went wrong: ";
		std::cout << e.what();
	}
	
	
	
	return(0);	
}
