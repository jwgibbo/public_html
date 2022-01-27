#include <iostream>

void recFunc(int i)
{
	if(i<=5)
	{
		recFunc(i+1); //recursive call
		std::cout << i << '\n';
	}
}


int main()
{	
	recFunc(1); //initial call
	std::cout << "Exiting...\n";
	
	return(0);
}