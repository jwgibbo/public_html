#include <iostream>

int main()
{
	std::cout << "i\tj\n";
	std::cout << "==========\n";
	for(int i=1; i<=4; i++)
	{
		for(int j=1; j<=3; j++)
		{
			std::cout << i << '\t' << j << '\n';
		}
		std::cout << "==========\n";
	}
	return(0);
}