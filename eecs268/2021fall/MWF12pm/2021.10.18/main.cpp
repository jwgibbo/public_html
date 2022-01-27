#include <iostream>

void recFunc(int i)
{
	if(i<5)
	{
		recFunc(i+1);//recursive call
		std::cout << i << '\n';
	}
}

//Board work
//define rec sum to take a positive int
//return sum from 1 to n
int recSum(int n)
{
	if(n==1)
	{
		return(1);
	}
	else
	{
		//your definition here:
		//example: sum 1 to n --> n + recSum(n-1)
		return(n+recSum(n-1));
	}
}

int main()
{
	//initial call
	recFunc(0);
	std::cout << "Exiting...\n";
	return(0);
}


