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
#include "DoubleLinkedList.h"

class Test
{
public:
	Test(std::ostream& os);
	void runTests();

	bool test1(); //size of empty list is zero  
	bool test2(); //size returns correct value after 1 pushFront
	bool test3(); //size returns correct value after 1 pushBack
	bool test4(); //size returns correct value after multiple pushFront
	bool test5(); //size returns correct value after multiple pushBack 
	bool test6(); //size returns correct value after adds and removeFront
	bool test7(); //size returns correct value after adds and removeBack 
	bool test8(); //find returns nullptr on empty list
	bool test9(); //find returns nullptr when value not in large list 
	bool test10(); //find returns pointer to node if value is in large list
	bool test11(); //printList prints nothing when printing empty list
	bool test12(); //printList prints the contents of large list correctly
	bool test13(); //removeFront on empty list returns false
	bool test14(); //removeBack on empty list returns false
	bool test15(); //size preserved by removeFront on populated list
	bool test16(); //size preserved by removeBack on populated list
	bool test17(); //size preserved by remove(value) on populated list	
	bool test18(); //order preserved by removeFront on populated list
	bool test19(); //order preserved by removeBack on poplulated list
	bool test20(); //remove(value) on empty list returns false
	bool test21(); //remove(value) where value is not in large list returns false
	bool test22(); //remove(value) where value is in large list returns true
	bool test23(); //order preserved by remove(value) on populated list
	bool test24(); //insertAhead on empty list throws exception
	bool test25(); //insertBehind on empty list throws exception
	bool test26(); //insertAhead of value not in list throws exception
	bool test27(); //insertBehind of value not in list throws exception
	bool test28(); //insertAhead of list size 1 retains list order
	bool test29(); //insertBehind of list size 1 retains list order
	bool test30(); //insertAhead on large list retains list order
	bool test31(); //insertBehind on large list retains list order
		
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
