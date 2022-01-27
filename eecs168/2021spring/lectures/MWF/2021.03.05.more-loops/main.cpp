#include <iostream>

int main()
{
	//Goal: Calculate the sum from 1 to 50000
	int sum = 0;
		
	for(int lcv=1; lcv<=5; lcv=lcv+1)
	{
		sum = sum + lcv;
	}
	
	std::cout << "Summation: " << sum << '\n';
	return(0);
}