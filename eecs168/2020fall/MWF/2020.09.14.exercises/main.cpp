#include<iostream>
//WARNING DO NOT COPY AND PASTE THIS CODE
//THE QUOTATIONS WILL NOT COMPILE
int main()
{
	int num;

	std::cout << “Insert number: “;
	std:: cin >> num;
	if (num < 0)
	{
		num = num * (-1);
	}
	std::cout << “Absolute value: “ << num << std::endl;
	return (0);
}
