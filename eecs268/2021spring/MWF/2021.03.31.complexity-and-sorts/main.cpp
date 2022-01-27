#include <iostream>

int main()
{	
	//Algorithm 1
	for(int i=0; i<10; i++)
	{
		std::cout << i << '\n';
	}
	
	std::cout << "END ALG 1\n";
	
	//Algorithm 2
	int n = 10;
	for(int i=0; i<n-1; i++)
	{
		std::cout << i << '\n';
	}
	
	std::cout << "END ALG 2\n";
	
	//Algorithm 3
	int size = 0;
	double* arr = nullptr;
	std::cout << "input a size: ";
	std::cin >> size;
	arr = new double[size];
	
	
	return(0);
}