#include <iostream>
#include <time.h>
#include <stdlib.h>
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
	int secretNum=0;
	int userGuess=0;
	
	
	secretNum = (rand()%10)+1;
	do
	{
		srand(time(NULL));
		
		std::cout << "What's your guess: ";
		std::cin >> userGuess;		
				
	}while(userGuess != secretNum);
	
	std::cout << "You guessed it!\n";
	
	return(0);
}