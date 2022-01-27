#include <iostream>

void recFunc(int i)
{
	if(i<5)
	{
		recFunc(i+1);//recursive call
		std::cout << i << '\n';
	}
}

int main()
{
	//initial call
	recFunc(0);
	std::cout << "Exiting...\n";]
	
	int i=0;
	while(i<5)
	{
		i = i + 1;
		std::cout << i << '\n';
	}
	
	return(0);
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
		//sum of 1 to 4 ==> 4 + recSum(3)
		//sum of 1 to 3 ==>     3 + recSum(2)
		//sum of 1 to 2 ==>         2 + recSum(1)
		//sum of 1 to 1 ==>             1
		return(n+recSum(n-1));
	}
}


