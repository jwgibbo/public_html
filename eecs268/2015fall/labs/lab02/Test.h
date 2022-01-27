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
#include "LinkedList.h"

class Test
{
public:
	Test(std::ostream& os);
	void runTests();

	bool test1(); //size of empty list is zero  
	bool test2(); //size returns correct value after 1 addFront
	bool test3(); //size returns correct value after 1 addBack
	bool test4(); //size returns correct value after multiple addFront
	bool test5(); //size returns correct value after multiple addBack 
	bool test6(); //size returns correct value after adds and removeFront
	bool test7(); //size returns correct value after adds and removeBack 
	bool test8(); //search returns false on empty list
	bool test9(); //search returns false when value not in list 
	bool test10(); //search returns true if value is in large list
	bool test11(); //printList prints nothing when printing empty list
	bool test12(); //printList prints the contents of large list correctly
	bool test13(); //removeFront on empty list returns false
	bool test14(); //removeBack on empty list returns false
	bool test15(); //size preserved by removeFront on populated list
	bool test16(); //size preserved by removeBack on populated list
	bool test17(); //order preserved by removeFront on populated list
	bool test18(); //order preserved by removeBack on poplulated list

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

};

#endif
