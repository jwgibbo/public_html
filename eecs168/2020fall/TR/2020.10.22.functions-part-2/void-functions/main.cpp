#include <iostream>

//declare the function:
void bananaPrint(int numPrints);

int main()
{
	//example call
	bananaPrint(5);//prints banana 5 times
	return(0);
}

//Define a function that prints
//the word "banana" as many times
//as the caller wants
void bananaPrint(int numPrints)
{
	for(int i=0; i<numPrints; i++)
	{
		std::cout << "banana\n";
	}
	
	//optional
	return;
}