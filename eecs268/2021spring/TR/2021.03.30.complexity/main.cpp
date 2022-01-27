#include <iostream>

int main()
{
	int sum = 0;
	for(int i=0; i<10; i++)
	{
		//do something
		sum += i;
	}
	
	int n=0;
	std::cout << "Input an n: ";
	std::cin >> n;
	sum = 0;
	for(int i=0; i<n; i++)
	{
		//do something
		sum += i;
	}
	
	return(0);
}