#include <iostream>
#include <stdexcept>
/* Situation: Our function promises to 
	return a value. But it can put into
	a situtation where that isn't possible.
	
	Solution: We need an alternative to 
	returning a value. 
	
	We will throw an exception
*/
double myDiv(double n1, double n2)
{
	if(n2 != 0)
	{
		return(n1/n2);
	}
	else
	{
		throw(std::runtime_error("Division by zero!\n"));
	}
}

double middleMan(double n1, double n2)
{
	double ans = myDiv(n1, n2);
	std::cout << "middleMan about to return\n";
	return(ans);
}

int main()
{
	double ans=0;
	
	//Try a risky thing
	try
	{
		//As soon as an exception is
		//thrown, go immediately to catch
		//block skipping any remaining
		//code
		ans = middleMan(10, 5);
		std::cout << ans << '\n';
		std::cout << "Phew! That was risky!\n";
	}
	catch (std::runtime_error& rte)
	{
		//The exception is caught.
		//This code only runs if an 
		//exception was thrown in the try
		//block
		std::cout << "Something went wrong.\n";
		std::cout << "Here the message from the exception: ";
		std::cout << rte.what() << '\n';
	}
	
	return(0);
}


/*BOARD WORK:
In a main.cpp, write a program that pretends a function called dangerous exits:
double dangerous(double n)

Until the user gives you a value that works, obtain a value from the user, pass it 
to dangerous, and print the value returned.  

You don't know what values make dangerous throw an exception, but it can.
*/