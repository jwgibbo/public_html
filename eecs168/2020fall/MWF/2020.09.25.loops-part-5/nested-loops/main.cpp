#include <iostream>

int main()
{
	for(int i=1; i<=3; i++)
	{		
		for(int j=1; j<=4; j++)
		{
			std::cout << "i = " << i << '\t';
			std::cout << "j = " << j << '\n';
		}
		std::cout << "inner loop finished\n";
	}
	
	return(0);
}