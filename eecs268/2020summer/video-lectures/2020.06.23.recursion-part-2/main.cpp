#include <iostream>

//GOAL: recursively print an array
void recPrint(int arr[], int size)
{
	if(size==1)
	{
		std::cout << arr[0] << '\n';
	}
	else
	{
		//print last element
		std::cout << arr[size-1] << '\n';
		//give the recursive call
		//the remainder of the array to print
		recPrint(arr, size-1);		
	}
}

/* 
5! = 5*4*3*2*1 	==> 5*4!
4! = 4*3*2*1	==> 4*3!	
3! = 3*2*1 		==> 3*2!
2! = 2*1		==> 2*1!
1! = 1
*/
int factorial(int n)
{
	//base case
	if(n<=1)
	{
		return(1);
	}
	else
	{
		return(n*factorial(n-1));
	}
}


//Board work
//define rec sum to take a positive int
//return sum from 1 to n
int recSum(int n)
{
	//Base case(s)
	if(n<=0)
	{
		return(0);
	}
	else
	{
		//Make a recursive call
		//Reduce the problem
		return(recSum(n-1) + n);
	}
}
/*
sum 1 to 1 ==> 1
sum 1 to 2 ==> sum(1) + 2
sum 1 to 3 ==> sum(2) + 3
sum 1 to 4 ==> sum(3) + 4
*/
int main()
{
	int ans = 0;
	
	ans = recSum(-1);//sum 1 to 4
	std::cout << "sum: " << ans << '\n';
	std::cout << "Exiting...\n";
	return(0);
}


