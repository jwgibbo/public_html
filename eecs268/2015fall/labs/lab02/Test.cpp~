#include "Test.h"

void Test::runTests()
{
	
	int score = 0;

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
	score += test10() ? 5 : 0; 
	score += test11() ? 2 : 0; 
	score += test12() ? 5 : 0; 
	score += test13() ? 2 : 0; 
	score += test14() ? 2 : 0; 
	score += test15() ? 5 : 0; 
	score += test16() ? 5 : 0; 
	score += test17() ? 5 : 0; 
	score += test18() ? 5 : 0; 
		
	std::cerr << "Score: " << score << " / " << MAX_SCORE << std::endl;
}


Test::Test(std::ostream& os) : os(os), TEST_SIZE(1000), NUM_TESTS(18), MAX_SCORE(70)
{
}


void Test::redirectOS()
{
	os_rdbuf = os.rdbuf(ss_redirect.rdbuf());
}


void Test::restoreOS()
{
	os.rdbuf(os_rdbuf);
}


bool Test::test1()
{
	LinkedList list;
	std::cerr << "Test 1: size of empty list is zero: ";

	if(list.size() == 0)
		std::cerr << "PASS" << std::endl;
	else
		std::cerr << "FAIL" << std::endl;

	return (list.size() == 0);
}


bool Test::test2()
{
	LinkedList list;

	list.addFront(1);

	std::cerr << "Test 2: size returns correct value after 1 add : ";

	if(list.size() == 1)
		std::cerr << "PASS" << std::endl;
	else
		std::cerr << "FAIL" << std::endl;

	return (list.size() == 1);
}




bool Test::test3()
{
	LinkedList list;
	std::cerr << "Test 3: size returns correct value after 1 addBack: ";

	list.addBack(5);
	
	if(list.size() == 1)
		std::cerr << "PASS" << std::endl;
	else
		std::cerr << "FAIL" << std::endl;
	
	return(list.size() == 1);	
}


bool Test::test4()
{
 	bool isPassed = false;
	LinkedList list;

	std::cerr << "Test 4: size returns correct value after multiple addFront:\n";


	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes "; 
		list.addFront(i);
		std::cerr.flush();
	}

	if( (list.size() == TEST_SIZE))
	{
		isPassed = true;
		std::cerr << "PASS" << std::endl;
	}
	else
	{
		isPassed = false;
		std::cerr << "FAIL" << std::endl;
	}

	return (isPassed); 
}


bool Test::test5()
{
	bool isPassed = false;
	LinkedList list;

	std::cerr << "Test 5: size returns correct value after multiple addBack:\n";


	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes "; 
		list.addBack(i);
		std::cerr.flush();
	}

	if( (list.size() == TEST_SIZE))
	{
		isPassed = true;
		std::cerr << "PASS" << std::endl;
	}
	else
	{
		isPassed = false;
		std::cerr << "FAIL" << std::endl;
	}

	return (isPassed); 

}


bool Test::test6()
{
	LinkedList list;
	int trackedSize = 0;
	bool isPassed=false;	

	std::cerr << "Test 6: size returns correct value after adds and removeFront: ";

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

	if(list.size() == trackedSize)
	{	
		isPassed = true;
		std::cerr << "PASS" << std::endl;
	}
	else
	{
		std::cerr << "FAIL" << std::endl;
	}

	return (isPassed);
}

bool Test::test7()
{
	LinkedList list;
	int trackedSize = 0;
	bool isPassed=false;	

	std::cerr << "Test 7: size returns correct value after adds and removeBack: ";

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
	
	if(list.size() == trackedSize)
	{	
		isPassed = true;
		std::cerr << "PASS" << std::endl;
	}
	else
	{
		std::cerr << "FAIL" << std::endl;
	}

	return (isPassed);
}

bool Test::test8()
{
	LinkedList list;
	bool isPassed = false;
	
	std::cerr << "Test 8: search returns false on empty list: ";

	if( !list.search(42) )
	{
		isPassed = true;
		std::cerr << "PASS" << std::endl;
	}
	else
	{
		std::cerr << "FAIL" << std::endl;
	}

	return (isPassed);
}

bool Test::test9()
{
	LinkedList list;
	bool isPassed = false;

	std::cerr << "Test 9: search returns false when value not in list: ";

	//add values from 0 to TEST_SIZE-1 inclusively
	for(int i=0; i<TEST_SIZE; i++)
	{
		list.addFront(i);
	}

	//search for value not in list
	if( !list.search(-1) )
	{
		isPassed = true;
		std::cerr << "PASS" << std::endl;
	}
	else
	{
		std::cerr << "FAIL" << std::endl;
	}

	return (isPassed);
}


bool Test::test10()
{
	LinkedList list;
	bool isPassed = true;

	std::cerr << "Test 10: search returns true when value when value in large list: \n";

	//Add values 0-(TEST_SIZE-1)
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes ";
		
		//Add every 50th node using addBack
		if( i%50 == 0) 
		{
			list.addBack(i);
		}
		else
		{
			list.addFront(i);
		}

		std::cerr.flush();
	}

	//Search for all added values. Set flag if any value is not found 
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tSearching " << (i+1) << "/" << TEST_SIZE << " nodes "; 
		if( !list.search(i) ) 
		{
			isPassed = false;
		}
		std::cerr.flush();
	}

	if(isPassed)
	{
		std::cerr << "PASS" << std::endl;
	}
	else
	{
		std::cerr << "FAIL" << std::endl;
	}

	return (isPassed);
}

bool Test::test11()
{
	LinkedList list;
	bool isPassed = false;

	redirectOS();
	ss_redirect.clear();
	list.printList();
	restoreOS();

	std::cerr << "Test 10: printList prints empty string for empty list: ";

	//Convert captured output to string and check length
	if(ss_redirect.str().length() == 0)
	{
		isPassed = true;
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return(isPassed);
}

bool Test::test12()
{
	LinkedList list;
	bool isPassed = true;
	int num=0;
	

	std::cerr << "Test 12: printList prints the contents of large list correctly \n";

	//Add values 0-(TEST_SIZE-1)
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes ";
		list.addBack(i);
		std::cerr.flush();
	}

	redirectOS();
	ss_redirect.clear();
	list.printList();
	restoreOS();
	
	//Check the order of the numbers produced by the printList call
	for(int i=0; i<TEST_SIZE; i++)
	{
		ss_redirect >> num;
		
		if( i!=num )
		{
			isPassed = false;
		}
	}

	if(isPassed)
	{
		std::cerr << "PASS" << std::endl;
	}
	else
	{
		std::cerr << "FAIL" << std::endl;
	}

	return (isPassed);
}

bool Test::test13()
{
	LinkedList list;
	bool isPassed = false;

	std::cerr << "Test 13: removeFront returns false on empty list: ";

	if( !list.removeFront() ) 
	{
		isPassed = true;
	}

	if(isPassed)
		std::cerr << "PASS" << std::endl;
	else
		std::cerr << "FAIL" << std::endl;

	return (isPassed);

}


bool Test::test14()
{
	LinkedList list;
	bool isPassed = false;

	std::cerr << "Test 14: removeBack returns false on empty list: ";

	if( !list.removeBack() ) 
		isPassed = true;

	if(isPassed)
		std::cerr << "PASS" << std::endl;
	else
		std::cerr << "FAIL" << std::endl;

	return (isPassed);
}

bool Test::test15()
{
	LinkedList list;
	bool isPassed = false;
	int trackedSize = 0;

	std::cerr << "Test 15: size preserved by removeFront on populated list:";

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

	if(trackedSize == list.size())
	{
		isPassed = true;
		std::cerr << "PASSED" << std::endl; 
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return (isPassed);
}


bool Test::test16()
{
	LinkedList list;
	bool isPassed = false;
	int trackedSize = 0;

	std::cerr << "Test 16: size preserved by removeBack on populated list:";

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

	if(trackedSize == list.size())
	{
		isPassed = true;
		std::cerr << "PASSED" << std::endl; 
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return (isPassed);
}

bool Test::test17()
{
	LinkedList list;
	bool isPassed = true;
	int num=0;
	

	std::cerr << "Test 17: order preserved by removeFront on populated list\n ";

	//Add values 0-(TEST_SIZE-1)
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes ";
		list.addBack(i);
		std::cerr.flush();
	}

	//Remove half of the node
	for(int i=0; i<TEST_SIZE/2; i++)
	{
		list.removeFront();
	}


	redirectOS();
	ss_redirect.clear();
	list.printList();
	restoreOS();
	
	//Check the order of the printed list
	for(int i=TEST_SIZE/2; i<TEST_SIZE; i++)
	{
		ss_redirect >> num;
		
		if( i!=num )
		{
			isPassed = false;
		}
	}

	if(isPassed)
	{
		std::cerr << "PASS" << std::endl;
	}
	else
	{
		std::cerr << "FAIL" << std::endl;
	}

	return (isPassed);
} 
bool Test::test18()
{
	LinkedList list;
	bool isPassed = true;
	int num=0;
	

	std::cerr << "Test 18: order preserved by removeBack on populated list\n ";

	//Add values 0-(TEST_SIZE-1)
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes ";
		list.addBack(i);
		std::cerr.flush();
	}

	//Remove half of the node
	for(int i=0; i<TEST_SIZE/2; i++)
	{
		list.removeBack();
	}


	redirectOS();
	ss_redirect.clear();
	list.printList();
	restoreOS();
	
	//Check the order of the printed list
	for(int i=0; i<TEST_SIZE/2; i++)
	{
		ss_redirect >> num;
		
		if( i!=num )
		{
			isPassed = false;
		}
	}

	if(isPassed)
	{
		std::cerr << "PASS" << std::endl;
	}
	else
	{
		std::cerr << "FAIL" << std::endl;
	}

	return (isPassed);
}

