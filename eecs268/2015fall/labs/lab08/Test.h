/**
*	@file Test.h
* 	@author Joseph St. Amand, John Gibbons
*	@date 2015.10.27
*
*/
#ifndef TEST_H
#define TEST_H

#include <iostream>
#include <vector>
#include <string>
#include <climits>
#include <algorithm> 

#include "BinarySearchTree.h"

class Test
{
public:
        Test();
        void runTests();

        bool test_isEmpty01();//isEmpty returns true on empty tree
        bool test_isEmpty02();//isEmpty returns false after a single add
	
	bool test_search01();//searching an empty tree returns false
	bool test_search02();//add(42) to empty tree then search(42) returns true
	bool test_search03();//add(42) to right subtree of root of then search(42) returns true
	bool test_search04();//add(42) to left subtree of root of then search(42) returns true
	bool test_search05();//searching for a value not in large tree returns false
	bool test_search06();//searching for all values in a large tree of random values; all searches return true

	bool test_clone01();//cloning an empty tree, deleting original, check that clone is empty
	bool test_clone02();//cloning a large tree, deleting original, searching for all values in copy

	bool test_order01();//vector returned by treeToVector(PRE_ORDER) returns vector: {50, 25, 10, 30, 75, 65, 100} 
	bool test_order02();//vector returned by treeToVector(IN_ORDER) returns vector: {10, 25, 30, 50, 65, 75, 100} 
	bool test_order03();//vector returned by treeToVector(IN_ORDER) returns vector: {10, 30, 25, 65, 100, 75, 50} 

	bool test_order04();//vector returned by treeToVector(PRE_ORDER) returns a vector with all values present in a large tree
	bool test_order05();//vector returned by treeToVector(IN_ORDER) returns a vector with all values present in a large tree
	bool test_order06();//vector returned by treeToVector(POST_ORDER) returns a vector with all values present in a large tree


private:
        int m_testNum;
        const int TEST_SIZE; //stress test size
        const int MAX_SCORE; //maximum points available from tests


        /**
        *  @pre None.
        *  @post Uses std::cerr to print the Pass/Fail message
        *  @return None.
        *
        */
        void printPassFail(bool isPassed) const;

        /**
        *  @pre None.
        *  @post Uses std::cerr to print the test number and description
        *  @return None.
        *
        */
        void printTestMessage(int testNum, std::string testDescription) const;


        /**
        *  @pre None.
        *  @post None.
        *  @return True if the file exists, false otherwise.
        *
        */
        bool isFileAccessible(std::string fileName) const;

        /**
        *  @pre None.
        *  @post None.
        *  @return True if the file exists, false otherwise.
        *
        */
        bool isSortedAscending(const std::vector<int>& vec) const;

        /**
        *  @pre None.
        *  @post None.
        *  @return True if the file exists, false otherwise.
        *
        */
        bool isSortedDescending(const std::vector<int>& vec) const;

        /**
        *  @pre The vector is empty.
        *  @post The vector is filled with the amount of unique random ints, 0 to MAX_INT inclusive 
	*  TODO (Not a todo for you dear student) Improve efficiency checking for unique values.
	*	   See Knuth or Floyd algorithms
        *
        */
	void uniqueRandomFill(std::vector<int>& vec, std::size_t amount);
	
        /**
        *  @pre None.
        *  @post The values in vec are added to the bst
        *
        */
	void loadVectorIntoTree(const std::vector<int>& vec, BSTI<int>* bst);

        /**
        *  @pre None.
        *  @post The vector is printed.
        *
        */
	void printVector(const std::vector<int>& vec);	

};

#endif
