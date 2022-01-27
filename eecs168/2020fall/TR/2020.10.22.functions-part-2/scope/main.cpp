#include <iostream>

//Function definition
int plusOne(int num)
{
	int ans = 0;
	ans = num + 1;
	//FREEZE POINT 1
	return(ans);	
}

int main()
{
	int prev = 5;
	int next = 0;
	
	next = plusOne(prev);
	//FREEZE POINT 2
	std::cout << next << '\n';
	
	next = plusOne(99);
	std::cout << next << '\n';
	
	return(0);
}