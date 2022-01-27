#include <iostream>

//Include the exception library
#include <stdexcept>

int myDiv(int num, int denom)
{
	if(denom != 0)
	{
		return (num/denom);
	}
	else
	{
		//We have no good value to return
		//Instead of a return we throw an 
		//exception
		throw(std::runtime_error("Division by zero"));
	}
}

int main()
{
	int ans = 0;
	
	try
	{
		ans = myDiv(10, 2);
		std::cout << "ans = " << ans << '\n';
	}
	catch(std::runtime_error& rte)
	{
		std::cout << "Something went wrong!\n";
		std::cout << rte.what() << '\n';
	}

	return(0);
}




