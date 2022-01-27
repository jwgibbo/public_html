/**
*	@file Test.h
* 	@author Joseph St. Amand, John Gibbons
*	@date 2015.08.27
*
*/
#ifndef TEST_H
#define TEST_H

#include <iostream>
#include <sstream>
#include <vector>
#include "Stack.h"

class Test
{
public:
	Test(std::ostream& os);
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
	*  ostream capture code written by Joseph St. Amand
	*
	*/
	std::ostream& os;
	std::stringstream ss_redirect;
	std::streambuf* os_rdbuf;

	const int TEST_SIZE; //stress test size
	const int NUM_TESTS; //number of tests
	const int MAX_SCORE; //maximum points available from tests

	inline void redirectOS();
	inline void restoreOS();

	void loadValues(Stack<int>& stack);
	void printPassFail(bool isPassed);
	void printTestMessage(int testNum, std::string testDescription);

};

#endif
