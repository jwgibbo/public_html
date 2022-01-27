#include <iostream>

void recFunc(int i)
{
	std::cout << "Hello from " << i << '\n';
	
	if(i<3)
	{
		recFunc( i+1 );		
	}

	std::cout << "Goodbye from " << i << '\n';	
}

int main()
{
	recFunc(0);//initial call
	std::cout << "Exiting...\n";
	return(0);
}