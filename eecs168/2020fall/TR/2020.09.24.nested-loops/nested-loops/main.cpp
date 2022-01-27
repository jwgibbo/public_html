#include <iostream>

int main()
{
	for(int i=1; i<4; i++)
	{
		for(int j=1; j<5; j++)
		{
			std::cout << "i= " << i << "\tj= " << j << '\n';	
		}
		
		std::cout << "Inner loop over\n";
		
	}
	
	return(0);
}