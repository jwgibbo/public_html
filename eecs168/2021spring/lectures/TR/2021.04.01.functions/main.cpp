#include <iostream>
#include <math.h>

//Goal: Define a function that takes 
//		an int and returns that int + 1
int plusOne(int num)
{
	int ans = 0;
	ans = num+1;	
	return(ans);
}


int main()
{
	double ans = 0;

	ans = plusOne(81);
	
	std::cout << ans << '\n';
	return(0);
}

