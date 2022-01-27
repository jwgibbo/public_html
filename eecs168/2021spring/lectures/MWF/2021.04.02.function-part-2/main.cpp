#include <iostream>
#include <math.h>

//Goal: Define a function that takes
//      an int and returns that int + 1
int successor(int num)
{
	int ans = 0;
	ans = num + 1;
	//STOP
	return(ans);//function ends
}

//GOAL: Define a function that takes
//		an int and prints the word "banana"
//		that number of times
void printBanana(int numPrints)
{
	for(int i=0; i<numPrints; i++)
	{
		std::cout << "Banana!\n";
	}
	return;//empty return
}

int main()
{
	int num = 5;
	printBanana(num);
	printBanana(num*num);
	return(0);//zero indicates success
}