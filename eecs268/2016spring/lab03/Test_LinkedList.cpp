/**
*	@file Test.cpp
* 	@author John Gibbons
*	@since 2016.02.02
*
*/


#include "Test_LinkedList.h"

void Test_LinkedList::runTests()
{
	
	int score = 0;
	const int MAX_SCORE = 90;

	std::cerr << "\n\n=========================\n";
	std::cerr << "   RUNNING TEST SUITE    \n";
	std::cerr << "=========================\n\n";

	//Run test and award points where appropriate
	score += test1() ? 2 : 0; 
	score += test2() ? 2 : 0; 
	score += test3() ? 3 : 0; 
	score += test4() ? 5 : 0; 
	score += test5() ? 5 : 0; 
	score += test6() ? 5 : 0; 
	score += test7() ? 5 : 0; 
	score += test8() ? 2 : 0; 
	score += test9() ? 5 : 0; 	
	score += test10() ? 10 : 0; 
	score += test11() ? 2 : 0; 
	score += test12() ? 5 : 0; 
	score += test13() ? 2 : 0; 
	score += test14() ? 2 : 0; 
	score += test15() ? 5 : 0; 
	score += test16() ? 10 : 0; 
	score += test17() ? 10 : 0; 
	score += test18() ? 10 : 0; 
	
	std::cerr << "Score: " << score << " / " << MAX_SCORE << std::endl;
}


Test_LinkedList::Test_LinkedList(int testSize) : Test(testSize)
{
}

void Test_LinkedList::loadList(const std::vector<int>& testValues, LinkedList& list) const
{
	for(std::size_t i=0; i<testValues.size(); i++)
	{	
		list.addBack( testValues[i] );	
	}
}

bool Test_LinkedList::test1()
{
	LinkedList list;
	bool isPassed = false;

	printTestMessage("size of empty list is zero"); 

	isPassed = list.size() == 0;
	printPassFail(isPassed);

	return (list.size() == 0);
}


bool Test_LinkedList::test2()
{
	LinkedList list;
	bool isPassed = false; 

	list.addFront(1);

	printTestMessage("size returns correct value after 1 addFront");

	isPassed = list.size() == 1;

	printPassFail(isPassed);
	return (isPassed);
}




bool Test_LinkedList::test3()
{
	LinkedList list;
	bool isPassed = false;

	printTestMessage("size returns correct value after 1 addBack");

	list.addBack(5);
	
	isPassed = list.size() == 1;
	
	printPassFail(isPassed);
	return(isPassed);	
}


bool Test_LinkedList::test4()
{
 	bool isPassed = false;
	LinkedList list;
	std::vector<int> vec;

	printTestMessage("size returns correct value after multiple addFront");


	std::cerr << std::endl;
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes "; 
		list.addFront(i);
		std::cerr.flush();
	}

	isPassed = list.size() == TEST_SIZE;

	printPassFail(isPassed);
	return (isPassed); 
}


bool Test_LinkedList::test5()
{
	bool isPassed = false;
	LinkedList list;
	std::vector<int> vec;
	printTestMessage("size returns correct value after multiple addBack");

	std::cerr << std::endl;
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes "; 
		vec.push_back(i);
		std::cerr.flush();
	}
	
	loadList(vec, list);
	
	isPassed = list.size() == TEST_SIZE;
	printPassFail(isPassed);
	return (isPassed); 
}


bool Test_LinkedList::test6()
{
	LinkedList list;
	int trackedSize = 0;
	bool isPassed=false;	

	printTestMessage("size returns correct value after adds and removeFront");

	//Mix of adding to the front, back and removing back
	for(int i = 0; i < TEST_SIZE; i++)
	{
		if(i%2 == 0)
		{
			list.addBack(i);
			trackedSize++;	
		}
		else if(i%3 == 0)
		{
			list.removeFront();
			trackedSize--;
		}
		else
		{
			list.addFront(i);
			trackedSize++;
		}
	}

	isPassed = list.size() == trackedSize;
	printPassFail(isPassed);
	return (isPassed); 
}

bool Test_LinkedList::test7()
{
	LinkedList list;
	int trackedSize = 0;
	bool isPassed=false;	

	printTestMessage("size returns correct value after adds and removeBack");

	//Mix of adding to the front, back and removing back
	for(int i = 0; i < TEST_SIZE; i++)
	{
		if(i%2 == 0)
		{
			list.addBack(i);
			trackedSize++;	
		}
		else if(i%3 == 0)
		{
			list.removeBack();
			trackedSize--;
		}
		else
		{
			list.addFront(i);
			trackedSize++;
		}
	}
	
	isPassed = list.size() == trackedSize;
	printPassFail(isPassed);
	return (isPassed); 
}

bool Test_LinkedList::test8()
{
	LinkedList list;
	bool isPassed = false;
	
	printTestMessage("search returns false on empty list");

	isPassed = !list.search(42);
	printPassFail(isPassed);
	return (isPassed); 
}

bool Test_LinkedList::test9()
{
	LinkedList list;
	bool isPassed = false;

	printTestMessage("search returns false when value not in list");

	//add values from 0 to TEST_SIZE-1 inclusively
	for(int i=0; i<TEST_SIZE; i++)
	{
		list.addFront(i);
	}

	//search for value not in list
	isPassed = !list.search(-1);
	printPassFail(isPassed);
	return (isPassed); 
}


bool Test_LinkedList::test10()
{
	LinkedList list;
	bool isPassed = true;

	printTestMessage("search returns true when value when value in large list");
	std::cerr << std::endl;
	//Add values 0-(TEST_SIZE-1)
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes ";
		
		//Add every other node using addBack
		if( i%2 == 0) 
		{
			list.addBack(i);
		}
		else
		{
			list.addFront(i);
		}

		std::cerr.flush();
	}

	std::cerr << std::endl;
	//Search for all added values. Set flag if any value is not found 
	for(int i=0; i<TEST_SIZE && isPassed; i++)
	{
		std::cerr << '\r' << "\tSearching " << (i+1) << "/" << TEST_SIZE << " nodes "; 
		if( !list.search(i) ) 
		{
			isPassed = false;
			std::cerr << "Search returned false for value: " << i << std::endl;
		}
		std::cerr.flush();
	}

	printPassFail(isPassed);
	return (isPassed); 
}

bool Test_LinkedList::test11()
{
	LinkedList list;
	bool isPassed = false;
	std::vector<int> vec;

	printTestMessage("toVector returns empty vector for empty list");
	
	vec = list.toVector();
	isPassed = vec.empty();
	printPassFail(isPassed);
	return (isPassed); 
}

bool Test_LinkedList::test12()
{
	LinkedList list;
	bool isPassed = true;
	std::vector<int> key;
	std::vector<int> test;
	

	printTestMessage("toVector creates vector with the contents of large list");

	std::cerr << std::endl;
	//Add values 0-(TEST_SIZE-1)
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes ";

		list.addBack(i);
		key.push_back(i);

		std::cerr.flush();
	}

	test = list.toVector();
	
	isPassed = test == key;

	if(!isPassed)
	{
		std::cerr << "ERROR: expected the following vector: " << std::endl;
		printVector(key);

		std::cerr << "vector produced by LinkedList class: " << std::endl;
		printVector(test);
	}
	
	printPassFail(isPassed);
	return (isPassed); 
}

bool Test_LinkedList::test13()
{
	LinkedList list;
	bool isPassed = false;

	printTestMessage("removeFront returns false on empty list");

	isPassed = !list.removeFront();
	printPassFail(isPassed);
	return (isPassed); 
}


bool Test_LinkedList::test14()
{
	LinkedList list;
	bool isPassed = false;

	printTestMessage("removeBack returns false on empty list");

	isPassed = !list.removeBack();
	printPassFail(isPassed);
	return (isPassed); 
}

bool Test_LinkedList::test15()
{
	LinkedList list;
	bool isPassed = false;
	int trackedSize = 0;

	printTestMessage("size preserved by removeFront on populated list");

	//Remove front on every 3rd iteration, add otherwise.
	for(int i=0; i<TEST_SIZE; i++)
	{
		if( i>0 && i%3 == 0)
		{

			list.removeFront();
			trackedSize--;
		}
		else
		{

			list.addFront(i);
			trackedSize++;
		}
	}

	isPassed = trackedSize == list.size();
	printPassFail(isPassed);
	return (isPassed); 
}


bool Test_LinkedList::test16()
{
	LinkedList list;
	bool isPassed = false;
	int trackedSize = 0;

	printTestMessage("size preserved by removeBack on populated list");

	//Remove front on every 3rd iteration, add otherwise.
	for(int i=0; i<TEST_SIZE; i++)
	{
		if( i>0 && i%3 == 0)
		{

			list.removeBack();
			trackedSize--;
		}
		else
		{

			list.addBack(i);
			trackedSize++;
		}
	}

	isPassed = trackedSize == list.size();
	printPassFail(isPassed);
	return (isPassed); 
}

bool Test_LinkedList::test17()
{
	LinkedList list;
	bool isPassed = true;
	std::vector<int> key;
	std::vector<int> test;
	

	printTestMessage("order preserved by removeFront on populated list");

	std::cerr << std::endl;
	//Add values 0-(TEST_SIZE-1)
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes ";
		list.addBack(i);
		key.push_back(i);
		std::cerr.flush();
	}

	//Remove half of the node
	for(int i=0; i<TEST_SIZE/2; i++)
	{
		key.erase(key.begin());
		list.removeFront();
	}

	test = list.toVector();
	isPassed = key == test;
	
	if(!isPassed)
	{
		std::cerr << "ERROR: expected the following vector: " << std::endl;
		printVector(key);

		std::cerr << "vector produced by LinkedList class: " << std::endl;
		printVector(test);
	}

	printPassFail(isPassed);
	return (isPassed); 
} 
bool Test_LinkedList::test18()
{
	LinkedList list;
	bool isPassed = true;
	std::vector<int> key;
	std::vector<int> test;

	printTestMessage("order preserved by removeBack on populated list");

	std::cerr << std::endl;
	//Add values 0-(TEST_SIZE-1)
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes ";
		list.addBack(i);
		key.push_back(i);
		std::cerr.flush();
	}

	//Remove half of the node
	for(int i=0; i<TEST_SIZE/2; i++)
	{
		list.removeBack();
		key.pop_back();
	}

	test = list.toVector();
	isPassed = key == test;

	if(!isPassed)
	{
		std::cerr << "ERROR: expected the following vector: " << std::endl;
		printVector(key);

		std::cerr << "vector produced by LinkedList class: " << std::endl;
		printVector(test);
	}

	printPassFail(isPassed);
	return (isPassed); 
}

