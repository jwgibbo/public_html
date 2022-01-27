#include <iostream>
#include <stdlib.h>
#include <time.h>

int main()
{
	int random = 0;
	
	srand(time(NULL));
	
	std::cout << "Current time: " << time(NULL) << '\n';
	
	for(int i=1; i<=5; i++)
	{
		random = (rand()%6)+1;
		std::cout << "random number = ";
		std::cout << random << '\n';
	}
	
	
	return(0);
}
