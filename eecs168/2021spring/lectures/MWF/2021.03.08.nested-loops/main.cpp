#include <iostream>

int main()
{
	//Goal print a 3x4 block of ?'s
	/*
	????
	????
	????
	*/
	
	//Baby's first goal:
	//Just print a single row of 4 ?'s

	for(int i=1; i<=5; i++)
	{
		for(int j=1; j<=7; j++)
		{
			std::cout << '?';	
		}
		std::cout << std::endl;
	}	
		
	return(0);
}