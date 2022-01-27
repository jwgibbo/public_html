#include <iostream>

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

	return(0);
}

