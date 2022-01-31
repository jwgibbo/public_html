/**
*	@file Test.cpp
* 	@author John Gibbons
*	@since 2015.11.17
*
*/


#include "Test.h"

Test::Test(int testSize) : TEST_SIZE(testSize), m_testNum(0)
{
}

void Test::printPassFail(bool isPassed) const
{
        if(isPassed)
                std::cerr << "PASSED" << std::endl;
        else
                std::cerr << "FAILED" << std::endl;
}

void Test::printTestMessage(std::string testDescription)
{	
	m_testNum++;
        std::cerr << "Test " << m_testNum << ": " << testDescription << ": ";
}

void Test::printVector(const std::vector<int>& vec) const
{
	std::cerr << "{";
	for(std::size_t i=0; i<vec.size(); i++)
	{
		std::cerr << vec[i];
		if(i != vec.size()-1)
		{
			std::cerr << ",";
		}
	}
	std::cerr << "}";	
}

void Test::printExpectedError(const std::vector<int>& expected, const std::vector<int>& given) const
{
	std::cerr << "ERROR!" << std::endl << "expected:" << std::endl;
	printVector(expected);
	std::cerr << std::endl << "given:" << std::endl;
	printVector(given);
	std::cerr << std::endl;	
}


bool Test::isSortedAscending(const std::vector<int>& vec) const
{
        bool isSorted = true;

        for(std::size_t i=0; i<vec.size()-1; i++)
        {
                if(vec[i] > vec[i+1])
                {
                        isSorted = false;
                }
        }

        return(isSorted);
}

bool Test::isSortedDescending(const std::vector<int>& vec) const
{
        bool isSorted = true;

        for(std::size_t i=0; i<vec.size()-1; i++)
        {
                if(vec[i] < vec[i+1])
                {
                        isSorted = false;
                }
        }

        return(isSorted);
}

void Test::uniqueRandomFill(std::vector<int>& vec, std::size_t amount)
{
	const int LIMIT = sqrt(INT_MAX) < TEST_SIZE ? INT_MAX : TEST_SIZE*TEST_SIZE;
	std::random_device randomDevice;	
	std::default_random_engine generator(randomDevice());
	std::uniform_int_distribution<int> distribution(0,LIMIT);
	int rand = 0;
	std::size_t numAdded = 0;

	while(numAdded < amount)
	{
		rand = distribution(generator);
		if( std::find(vec.begin(), vec.end(), rand) == vec.end() )
		{
			vec.push_back(rand);
			numAdded++;
		}
	}
}
