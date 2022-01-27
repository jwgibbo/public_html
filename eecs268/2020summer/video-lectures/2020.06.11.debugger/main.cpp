#include <iostream>
#include "Node.h"
#include "Queue.h"

int main()
{
	/*
		$>gdb ./prog
		
		commands in gdb:
		break fileName:lineNumber
		run
		print variable name
		print *pointerToArray@sizeOfArray
		print object.memberVariable
		info locals
		next
		step
		disable
		continue
		shell clear
		quit
	*/

	int size = 5;
	int* ptr = new int[size];  
	for(int i=0; i<size; i++)
	{
		ptr[i] = 10*(i+1);
	}

	
	Queue<int> myQ; //constructor runs
	myQ.enqueue(5);
	myQ.enqueue(10);
	
	
	/*
		1) print a variable
		2) print what a pointer is pointing to
		3) print an array
		4) print a member variable
	*/
	return(0);
}

