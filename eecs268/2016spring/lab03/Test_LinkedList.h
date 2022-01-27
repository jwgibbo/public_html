/**
*	@file Test.h
* 	@author John Gibbons
*	@since 2016.02.02
*
*/
#ifndef TEST_LINKED_LIST_H
#define TEST_LINKED_LIST_H

#include <iostream>
#include <vector>
#include "LinkedList.h"
#include "Test.h"

class Test_LinkedList : public Test
{
public:
	Test_LinkedList(int testSize);
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
	bool test11(); //toVector returns empty vector for empty list: 
	bool test12(); //toVector creates vector with the contents of large list 
	bool test13(); //removeFront on empty list returns false
	bool test14(); //removeBack on empty list returns false
	bool test15(); //size preserved by removeFront on populated list
	bool test16(); //size preserved by removeBack on populated list
	bool test17(); //order preserved by removeFront on populated list
	bool test18(); //order preserved by removeBack on poplulated list

private:
	/**
	*	@pre none
	*	@post the list has the values in testValues added using addBack
	*/
	void loadList(const std::vector<int>& testValues, LinkedList& list) const;
};

#endif
