#include <iostream>
#include <math.h>

//Goal: define a function that takes
// and integer and calculates and 
// returns that integer+1
int addOne(int num)
{
	//declare a local variable
	int ans = 0;
	ans = num + 1;
	//FREEZE CODE
	//Draw call stack and heap
	return( ans );
}


int main()
{
	int prev = 5;
	int next = 0;
	
	//On the call, the parameter
	//gets a value
	next = addOne(prev);
	
	std::cout << "next = " << next << '\n';
	return(0);
}

