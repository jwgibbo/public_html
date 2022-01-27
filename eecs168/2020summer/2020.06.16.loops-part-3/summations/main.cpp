#include <iostream>

int main()
{
	//Goal: Sum up the value from 1 to 5
	//      Then print the sum.
	
	int sum = 0;//track the running total
	
	for(int i=1; i<=5; i=i+1)
	{
		//sum =  (old sum)+(i's current value) 
		sum = sum + i;
		
		std::cout << "i = " << i;
		std::cout << " sum = " << sum << '\n';
		
	}
	return(0);
}

/* Board work
Make a program that calculates the factorial of a 
number (assume small values from the user)
(HINT 5! = 1*2*3*4*5)

$>./prog
Calculate the factorial of what value?: 5
Factorial of 5 = 120
*/