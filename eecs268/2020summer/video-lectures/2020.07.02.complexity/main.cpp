#include <iostream>


int main()
{
	int n=0;
	
	
	//Loop always runs 100 times
	for(int i=0; i<100; i++)
	{
		//do something
	}

	
	//loop that scales with n
	//in a linear way

	
	
	std::cout << "Input an n: ";
	std::cin >> n;
	int temp = 0;
	for(int i=0; i<n; i++)
	{
		temp = i - i;
	}
	
	
	
	//nested loop scales with n
	//quadratically (n^2)
	std::cout << "Input an n: ";
	std::cin >> n;
	int temp = 0;
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<n; j++)
		{
			temp = i - i;
		}
	}
	
	
	
	//triple nested loop scales with n
	//in an n^3 way
	std::cout << "Input an n: ";
	std::cin >> n;
	int temp = 0;
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<n; j++)
		{
			for(int k=0; k<n; k++)
			{
				temp = i - i;
			}
		}
	}
	
	//Memory complexity that scales with n, O(n)
	std::cout << "Input an n: ";
	std::cin >> n;
	int* ptr = new int[n];//n element array
	
	//Memory complexity that scales with n, O(n^2)
	std::cout << "Input an n: ";
	std::cin >> n;
	int** grid = new int*[n];//n element array
	for(int i=0; i<n; i++)
	{
		grid[i] = new int[n];
	}
	return(0);
}

