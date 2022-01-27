#include <iostream>
#include <string>

int nextNum(int num)
{
	int ans = 0;
	ans = num + 1;
	
	//FREEZE! draw the call stack
	
	return(ans);
}

bool isOdd(int num)
{
	return(num%2 == 1);
}

void bananalib(std::string place)
{
	std::cout << "I eat bananas in the ";
	std::cout << place << '\n';
	return;
}

int main()
{
	int num = 0;
	
	num = nextNum(5);
	std::cout << num << '\n';
	return(0);
}