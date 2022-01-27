#include <iostream>

int main()
{
	for(int i=1; i<=3; i=i+1)
	{
		//for every value of i, the 
		//entire inner loop runs
		for(int j=1; j<=5; j=j+1)
		{
			std::cout << "i= " << i << '\t';
			std::cout << "j= " << j << '\n';
		}
		
		std::cout << "Inner loop finished\n";
	}
	return(0);
}

/*Nested loop board works:
1) Print the following grid of numbers to terminal

$>./prog
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20

2) Let the user give you the n for an nXn grid size
   Print a grid of *'s based on the user's size
   Force the user to give a positive grid size
   (HINT: while loops)
$>./prog
Input grid size: 4
****
****
****
****

*/