/**
*	@file Test.h
* 	@author John Gibbons
*	@date 2015.11.17
*
*/
#ifndef TEST_H
#define TEST_H

#include <iostream>
#include <vector>
#include <string>
#include <climits>
#include <algorithm> 
#include <math.h>
#include <random>

class Test
{
public:
	Test(int testSize);
	virtual void runTests() = 0;

protected:

	const int TEST_SIZE; //stress test size
	int m_testNum; //current test number

        /**
        *  @pre None.
        *  @post Uses std::cerr to print the Pass/Fail message
        *  @return None.
        *
        */
        void printPassFail(bool isPassed) const;

        /**
        *  @pre None.
        *  @post Uses std::cerr to print the test number and description. testNum is incremented.
        *  @return None.
        *
        */
        void printTestMessage(std::string testDescription);

        /**
        *  @pre None.
        *  @post The vector is printed.
        *
        */
	void printVector(const std::vector<int>& vec) const;	

	/**
	*  @pre none
	*  @post prints error message with contents of expected vector and given vector
	*/
	void printExpectedError(const std::vector<int>& expected, const std::vector<int>& given) const;
	
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
        *  @post The vector is filled with the amount of unique random ints, 
	*	range: 0 to min(TEST_SIZE^2, MAX_INT) inclusive 
        *
        */
	void uniqueRandomFill(std::vector<int>& vec, std::size_t amount);

};

#endif
