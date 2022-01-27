
#include "Triangle.h"

int addOne(int num)
{
	int ans = num + 1;
	return (ans);
}

int main()
{
	int x = 5;
	x = 10;
	10 = x;//ERROR
	
	//When you allocate a Triangle the 
	//constructor is 
	Triangle tri1; //Constructor is called

	tri1.base = -5; //ERROR
	tri1.height = 10; //ERROR
	
	tri1.getBase() = -5;//ERROR
	
	tri1.setBase(-5);//Compiles
	
	std::cout << tri1.getBase() << '\n';
	
	std::cout << tri1.area() << '\n';
	
	return(0);
}