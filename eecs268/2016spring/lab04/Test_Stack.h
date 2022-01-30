/**
*	@file Test.h
* 	@author Joseph St. Amand, John Gibbons
*	@date 2015.08.27
*
*/
#ifndef TEST_STACK_H
#define TEST_STACK_H

#include <iostream>
#include <sstream>
#include <vector>
#include "Test.h"

#include "Stack.h"

class Test_Stack : public Test
{
public:
	Test_Stack(int testSize);
	void runTests();


	bool test1(); //size of empty stack is zero  
	bool test2(); //size returns correct value after 1 push
	bool test3(); //size returns correct value after lots of pushes
	bool test4(); //peek on empty stack throws exception
	bool test5(); //peek returns correct value on stack size 1
	bool test6(); //peek returns correct value after lots of pushes
	bool test7(); //pop on empty stack throws PreconditionViolationException exception
	bool test8(); //pop on stack of size 1 reduces size to zero
	bool test9(); //size remains accurate after lots of pushes and pops
	bool test10(); //print on empty list print empty string
	bool test11(); //print after lots of pushes retains order
	bool test12(); //print after lots of pushes, pops, and peeks retains order

		
private:
	/**
	*	@pre none
	*	@post  loads the stack with test values
	*	@return a vectors with the same value (front being the top value)
	*/
	std::vector<int> loadValues(Stack<int>& stack);
};

#endif
