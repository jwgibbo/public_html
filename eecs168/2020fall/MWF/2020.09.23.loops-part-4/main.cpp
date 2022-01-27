#include <iostream>

int main()
{
	
	//Goal: calculate the sum
	//of 1 to 5
	
	int sum = 0;
	
	std::cout << "i\t\tsum\n";
	for(int i=1; i <= 5; i = i + 1)
	{
		sum = sum + i;
		std::cout << i << "\t\t" << sum << '\n';
	}
	
	std::cout << "sum = " << sum << '\n';
	
	return(0);
}