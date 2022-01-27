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
		throw( std::runtime_error("Div by zero") );
	}
}

int main()
{
	int num=0;
	
	try
	{
		num = myDiv(10, 0);
		std::cout << num << '\n';
	}
	catch(std::runtime_error& rte)
	{
		//handle the error
		std::cout << "Something went wrong:\n";
		std::cout << rte.what() << '\n';
	}
	
	
	return(0);
}