#include <iostream>

int main()
{	
	//Goal: create a program that 
	//asks the user if they want 
	//to quit. Exit if they type
	//Q or q
	
	char choice = '\0';
	int upperBound = 0;
	do
	{
		std::cout << "How high should I count?: ";
		std::cin >> upperBound;
		
		for(int i=1; i<=upperBound; i=i+1)
		{
			std::cout << i << '\n';
		}
		
		
		std::cout << "Enter Q/q to quit: ";
		std::cin >> choice;	
	}while(choice!='Q' && choice!='q');
	
	std::cout << "Exiting...\n";
	
	return(0);
}