#include <iostream>


int main()
{
	//Goal: let the user create and fil
	//an array of chars
	
	//create the pointer
	char* symbols = nullptr;
	int size = 0;
	
	
	//obtain the size
	std::cout << "How many characters do you want to store?: ";
	std::cin >> size;
	
	//create the array
	symbols = new char[size];
	
	for(int i=0; i<size; i++)
	{
		std::cout << "Enter a char: ";
		std::cin >> symbols[i];
	}	
	
	for(int i=0; i<size; i++)
	{
		std::cout << symbols[i] << '\n';
	}
	
	delete[] symbols;
	
	return(0);
}
