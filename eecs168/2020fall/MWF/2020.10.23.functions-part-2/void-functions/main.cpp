#include <iostream>

//Define a function that prints
//the word banana some number of 
//times that's based on a parameter
void bananaPrint(int numPrints)
{
	for(int i=0; i<numPrints; i++)
	{
		std::cout << "banana\n";
	}
	//using return is optional
	return;
}

int main()
{
	//On the call, the parameter
	//receives a value
	bananaPrint(10);
	
	double ans = sqrt(9);
	

	return(0);
}


