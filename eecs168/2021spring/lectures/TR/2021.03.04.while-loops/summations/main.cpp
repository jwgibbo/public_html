#include <iostream>

int main()
{
	//Goal: Calculate of sum of 1 to 5
	
	int sum = 0;
	
	for(int lcv=1; lcv<=5; lcv=lcv+1)
	{
		sum = sum + lcv;
	}
	
	std::cout << "Summation 1 to 5: " << sum;
	std::cout << '\n';
	
	return(0);
}
