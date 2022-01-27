//main.cpp

#include <iostream>
#include "Node.h"
#include "StackOfInts.h"

int main()
{
	StackOfInts myStack;
	
	myStack.push(20);
	myStack.push(5);
	myStack.push(15);
	myStack.pop();
	
	return(0);
}