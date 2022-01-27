/**
*	@file Test.h
* 	@author Joseph St. Amand, John Gibbons
*	@date 2015.10.13
*
*/
#ifndef TEST_H
#define TEST_H

#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include "Sorts.h"

class Test
{
public:
	Test(std::ostream& os);
	void runTests();

	bool test1(); //createTestArray creates an array of the requested size
	bool test2(); //createTestArray creates an array with values in the provided range

	bool test3(); //isSorted returns true when array size is one  
	bool test4(); //isSorted returns false when array is not sorted
	bool test5(); //isSorted returns false when array is sorted, but not ascending
	bool test6(); //isSorted returns true when array is sorted in ascending order

	bool test7(); //bubble sort called with an array of size 1
	bool test8(); //insertion sort called with an array of size 1
	bool test9(); //selection sort called with an array of size 1
	bool test10(); //bogo sort sorts called with an array of size 1

	bool test11(); //bubble sort sorts an array of size n in ascending order
	bool test12(); //insertion sort sorts an array of size n in ascending order
	bool test13(); //selection sort sorts an array of size n in ascending order
	bool test14(); //bogo sort sorts an array of size n in ascending order

	bool test15(); //bubble sort completes in reasonable amount of time (0-10s platform dependent)
	bool test16(); //insertion sort completes in reasonable amount of time (0-10s platform dependent)
	bool test17(); //selection sort completes in reasonable amount of time (0-10s platform dependent)
	
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

	void printPassFail(bool isPassed);
	void printTestMessage(int testNum, std::string testDescription);

};

#endif
