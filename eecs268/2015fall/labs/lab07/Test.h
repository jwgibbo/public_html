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
#include <fstream>

#include "Sorts.h"
#include "NumberFileGenerator.h"
#include "NumberFileDriver.h"
#include "SortDriver.h"

class Test
{
public:
	Test(std::ostream& os);
	void runTests();

	bool test_sort1(); //createTestArray creates an array of the requested size
	bool test_sort2(); //createTestArray creates an array with values in the provided range

	bool test_sort3(); //isSorted returns true when array size is one  
	bool test_sort4(); //isSorted returns false when array is not sorted
	bool test_sort5(); //isSorted returns false when array is sorted, but not ascending
	bool test_sort6(); //isSorted returns true when array is sorted in ascending order

	bool test_sort7(); //bubble sort called with an array of size 1
	bool test_sort8(); //insertion sort called with an array of size 1
	bool test_sort9(); //selection sort called with an array of size 1
	bool test_sort10(); //bogo sort sorts called with an array of size 1

	bool test_sort11(); //bubble sort sorts an array of size n in ascending order
	bool test_sort12(); //insertion sort sorts an array of size n in ascending order
	bool test_sort13(); //selection sort sorts an array of size n in ascending order
	bool test_sort14(); //bogo sort sorts an array of size n in ascending order

	bool test_sort15(); //bubble sort completes in reasonable amount of time (0-10s platform dependent)
	bool test_sort16(); //insertion sort completes in reasonable amount of time (0-10s platform dependent)
	bool test_sort17(); //selection sort completes in reasonable amount of time (0-10s platform dependent)

	bool test_sort18(); //merge sort called with an array of size 1
	bool test_sort19(); //quick sort called with an array of size 1
	bool test_sort20(); //quick3 sort called with an array of size 1

	bool test_sort21(); //merge sort sorts an array of size n in ascending order
	bool test_sort22(); //quick sort sorts an array of size n in ascending order
	bool test_sort23(); //quickWithMedian sort sorts an array of size n in ascending order
	
	bool test_sort24(); //merge sort completes in reasonable amount of time (0-2s platform dependent)
	bool test_sort25(); //quick sort completes in reasonable amount of time (0-2s platform dependent)
	bool test_sort26(); //quickWithMedian sort completes in reasonable amount of time (0-2s platform dependent)

	bool test_NumFileGen1(); //all files creation methods create file of desired name
	bool test_NumFileGen2(); //all files creation methods place the number of values written at top of file
	bool test_NumFileGen3(); //ascending method creates files with numbers in ascending order	
	bool test_NumFileGen4(); //descending method creates files with numbers in ascending order
	bool test_NumFileGen5(); //random method creates file with random (unsorted) values
	bool test_NumFileGen6(); //singleValue method creates files with all 1 value		

	bool test_NumFileDriver1(); //Testing for Number Driver "./prog -create -a filename amount"
	bool test_NumFileDriver2(); //Testing for Number Driver "./prog -create -d filename amount"
	bool test_NumFileDriver3(); //Testing for Number Driver "./prog -create -s filename amount value"
	bool test_NumFileDriver4(); //Testing for Number Driver "./prog -create -r filename amount low high"

	bool test_SortDriver1(); //Testing for Sort Driver "./prog -sort -bubble inputFile outputFile"
	bool test_SortDriver2(); //Testing for Sort Driver "./prog -sort -selection inputFile outputFile"
	bool test_SortDriver3(); //Testing for Sort Driver "./prog -sort -insertion inputFile outputFile"
	bool test_SortDriver4(); //Testing for Sort Driver "./prog -sort -merge inputFile outputFile"
	bool test_SortDriver5(); //Testing for Sort Driver "./prog -sort -quick inputFile outputFile"
	bool test_SortDriver6(); //Testing for Sort Driver "./prog -sort -quick3 inputFile outputFile"
	bool test_SortDriver7(); //Testing for Sort Driver "./prog -sort -all inputFile outputFile"

private:
	int m_testNum;

	/** 
	*  ostream capture code written by Joseph St. Amand
	*
	*/
	std::ostream& os;
	std::stringstream ss_redirect;
	std::streambuf* os_rdbuf;

        const int TEST_SIZE; //stress test size
        const int MAX_SCORE; //maximum points available from tests

	inline void redirectOS();
	inline void restoreOS();

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

};

#endif
