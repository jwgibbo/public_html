#include <iostream>

/*
Debugger commands:
$> gdb ./programNameHere

quit 
	-quits the debugger

break main.cpp:line#  
	-inserts a break point

next
	-run the next instruction/line of code

info local
	-print all local variables
	
shell clear
	-clean up the terminal

disable
	-turn off break points
	
continue 
	-unpause the program (until next breakpoint)
*/

int main()
{	
	int sum=0;
	int userNum=0;
	
	std::cout << "Input a number: ";
	std::cin >> userNum;
	
	for(int i=0; i<userNum; i++)
	{
		sum = sum + i;
	}
	
	std::cout << "sum = " << sum << '\n';
	
	return(0);
}