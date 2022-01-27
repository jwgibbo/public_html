#include <iostream>

int factorial(int n)
{
	if(n<=1)
	{
		return(1);
	}
	else
	{
		return(n*factorial(n-1));
	}
}


int main()
{
	
	int userNum = 0;
	//assume you get value from the user
	int ans = factorial(userNum);
	
	//There is no n that makes
	//this loop scale in time complexity
	for(int i=0; i<5; i++)
	{
		//do something
	}
	
	
	int n=????;
	for(int i=0; i<n; i++)
	{
		//do something
	}
	
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<n; j++)
		{
			//do something
		}
	}
	
	
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<n; j++)
		{
			for(int k=0; k<n; k++)
			{
				//do something
			}
		}
	}
	
	int userSize = 0;
	//assume we get the size from the user
	
	//O(1) space complexity
	int* constArray = new int[100];
	
	//O(n) space complexity
	int* variableArray = new int[userSize];
	
	
	
}