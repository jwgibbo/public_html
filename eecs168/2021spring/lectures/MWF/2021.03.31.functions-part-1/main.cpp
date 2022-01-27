#include <iostream>
#include <math.h>

//Goal: Define a function that takes
//      an int and returns that int + 1
int successor(int num)
{
	int nextNum = 0;
	nextNum = num + 1;
	return(nextNum);
}

int main()
{

	double ans = 0;
	
	//call the successor function
	ans = successor(54);
	ans = sqrt(81);
	std::cout << successor(1999) << '\n';
	return(0);
}