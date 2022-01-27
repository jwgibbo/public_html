#include <iostream>

int main()
{
	//Goal: Print the numbers 1 to 5 
	//to the screen 
	
	std::cout << 1 << '\n';
	std::cout << 2 << '\n';
	std::cout << 3 << '\n';
	std::cout << 4 << '\n';
	std::cout << 5 << '\n';
	
	for(int lcv=1; lcv<=5; lcv = lcv + 1)
	{
		std::cout << lcv << '\n';
	}
	
	
	return(0);
}