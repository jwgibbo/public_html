#include <iostream>
void bananaPrint(int num);
int plusOne(int num);

void byValueFunc(int num)
{
	std::cout << "Haha!\n";
	num = 99;
}

void byRefFunc(int& num)
{
	std::cout << "Haha!\n";
	num = 99;
}


int main()
{
	int num = 5;
	std::cout << "num=" << num << '\n';
	byValueFunc(num);
	std::cout << "num=" << num << '\n';
	byRefFunc(num);
	std::cout << "num=" << num << '\n';
	return(0);
}

//Goal: Define that takes in an int
//		and print "banana" that many times
void bananaPrint(int num)
{
	for(int i=0; i<num; i++)
	{
		std::cout << "banana\n";
	}
	//optional return
	return;
}

//Goal: Define a function that takes 
//		an int and returns that int + 1
int plusOne(int num)
{
	int ans = 0;
	ans = num+1;	
	return(ans);
}