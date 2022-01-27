#include <iostream>
#include <stdexcept>

int myDiv(int n1, int n2)
{
	if(n2 != 0)
	{
		return(n1/n2);
	}
	else
	{
		//throw an exception
		throw( std::runtime_error("Bananarama!") );
	}
}

int main()
{
	int num = 0;
	
	try
	{
		//call that passes in bad parameter
		num = myDiv(5, 0);
	}
	catch (std::runtime_error& rte)
	{
		std::cout << "Something went wrong: " << rte.what() << '\n';
	}
	
	
	std::cout << num << '\n';
	
	return(0);
}