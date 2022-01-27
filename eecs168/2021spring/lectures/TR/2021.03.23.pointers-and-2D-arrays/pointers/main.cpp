#include <iostream>


int main()
{
	int x = 5;
	int y = 0;
	y = x;//store 5 in y
	x = 10;//store 10 in x, but y is unchanged
	std::cout << y << '\n';//prints 5
	
	int nums[3];
	
	nums = nullptr; //COMPILER ERROR
	nums = new int[3]; //COMPILER ERROR
	
	char* symbols = nullptr;
	char* ptrB = nullptr;
	int size = 0;
	
	std::cout << "How many characters?: ";
	std::cin >> size;
	
	//create the array
	symbols = new char[size];
	ptrB = symbols;//Assigning a pointer to a pointer

	symbols[0] = 'A';
	std::cout << ptrB[0] << '\n';//prints 'A"
	ptrB[1] = 'Q';

		
	
	return(0);
}
