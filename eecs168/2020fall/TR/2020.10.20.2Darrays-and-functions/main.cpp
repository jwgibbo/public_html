#include <iostream>

//define a function that
//takes in an int and returns
//that int+1
int plusOne(int num)
{
	int ans = 0;
	ans = num + 1;
	//FREEZE CODE and
	//draw the 
	return(ans);
}


int main()
{
	int prev = 5;
	int next = 0;
	
	next = plusOne(54);

	std::cout << next << '\n';	
	
	return(0);
}