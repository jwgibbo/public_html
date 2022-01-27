#include <iostream>

void recFunc(int i)
{
	if(i<5)
	{	
		recFunc(i+1); //pass math
		std::cout << i << "\n";
	}	
}

int main()
{
	recFunc(0);//The initial call
			  //The initial value for i
	
	return(0);
}