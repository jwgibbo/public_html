#include <iostream>

void recFunc(int i)	
{	
	if(i<=5)
	{
		std::cout << i << "\n";
		recFunc(i+1);
	}
}

int main()
{	
	recFunc(1);//initial call
	return(0);
}