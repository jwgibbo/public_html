#include "Test.h"

void Test::runTests()
{
	
	int score = 0;

	std::cerr << "\n\n=========================\n";
	std::cerr << "   RUNNING TEST SUITE    \n";
	std::cerr << "=========================\n\n";

	//Run test and award points where appropriate
	score += test1() ? 1: 0; 
	score += test2() ? 1: 0; 
	score += test3() ? 1: 0; 
	score += test4() ? 2: 0; 
	score += test5() ? 2: 0; 
	score += test6() ? 2: 0; 
	score += test7() ? 2: 0; 
	score += test8() ? 1: 0; 
	score += test9() ? 2: 0; 
	score += test10() ? 2: 0; 
	score += test11() ? 1: 0; 
	score += test12() ? 3: 0; 
	score += test13() ? 1: 0; 
	score += test14() ? 1: 0; 
	score += test15() ? 2: 0; 
	score += test16() ? 2: 0; 
	score += test17() ? 3: 0; 
	score += test18() ? 3: 0; 
	score += test19() ? 3: 0; 
	score += test20() ? 2: 0; 
	score += test21() ? 2: 0; 
	score += test22() ? 3: 0; 
	score += test23() ? 5: 0; 
	score += test24() ? 2: 0; 
	score += test25() ? 2: 0; 
	score += test26() ? 3: 0; 
	score += test27() ? 3: 0; 
	score += test28() ? 2: 0; 
	score += test29() ? 2: 0; 
	score += test30() ? 7: 0; 
	score += test31() ? 7: 0; 


	std::cerr << "Score: " << score << " / " << MAX_SCORE << std::endl;
}


Test::Test(std::ostream& os) : os(os), TEST_SIZE(1000), NUM_TESTS(18), MAX_SCORE(75)
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
	DoubleLinkedList<int> list;
	std::cerr << "Test 1: size of empty list is zero: ";

	if(list.size() == 0)
		std::cerr << "PASSED" << std::endl;
	else
		std::cerr << "FAILED" << std::endl;

	return (list.size() == 0);
}


bool Test::test2()
{
	DoubleLinkedList<int> list;

	list.pushFront(1);

	std::cerr << "Test 2: size returns correct value after 1 add : ";

	if(list.size() == 1)
		std::cerr << "PASSED" << std::endl;
	else
		std::cerr << "FAILED" << std::endl;

	return (list.size() == 1);
}




bool Test::test3()
{
	DoubleLinkedList<int> list;
	std::cerr << "Test 3: size returns correct value after 1 pushBack: ";

	list.pushBack(5);
	
	if(list.size() == 1)
		std::cerr << "PASSED" << std::endl;
	else
		std::cerr << "FAILED" << std::endl;
	
	return(list.size() == 1);	
}


bool Test::test4()
{
 	bool isPassed = false;
	DoubleLinkedList<int> list;

	std::cerr << "Test 4: size returns correct value after multiple pushFront:\n";


	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes.  "; 
		list.pushFront(i);
		std::cerr.flush();
	}

	if( (list.size() == TEST_SIZE))
	{
		isPassed = true;
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		isPassed = false;
		std::cerr << "FAILED" << std::endl;
	}

	return (isPassed); 
}


bool Test::test5()
{
	bool isPassed = false;
	DoubleLinkedList<int> list;

	std::cerr << "Test 5: size returns correct value after multiple pushBack:\n";


	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes.  "; 
		list.pushBack(i);
		std::cerr.flush();
	}

	if( (list.size() == TEST_SIZE))
	{
		isPassed = true;
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		isPassed = false;
		std::cerr << "FAILED" << std::endl;
	}

	return (isPassed); 

}


bool Test::test6()
{
	DoubleLinkedList<int> list;
	int trackedSize = 0;
	bool isPassed=false;	

	std::cerr << "Test 6: size returns correct value after adds and removeFront: ";

	//Mix of adding to the front, back and removing back
	for(int i = 0; i < TEST_SIZE; i++)
	{
		if(i%2 == 0)
		{
			list.pushBack(i);
			trackedSize++;	
		}
		else if(i%3 == 0)
		{
			list.removeFront();
			trackedSize--;
		}
		else
		{
			list.pushFront(i);
			trackedSize++;
		}
	}

	if(list.size() == trackedSize)
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

bool Test::test7()
{
	DoubleLinkedList<int> list;
	int trackedSize = 0;
	bool isPassed=false;	

	std::cerr << "Test 7: size returns correct value after adds and removeBack: ";

	//Mix of adding to the front, back and removing back
	for(int i = 0; i < TEST_SIZE; i++)
	{
		if(i%2 == 0)
		{
			list.pushBack(i);
			trackedSize++;	
		}
		else if(i%3 == 0)
		{
			list.removeBack();
			trackedSize--;
		}
		else
		{
			list.pushFront(i);
			trackedSize++;
		}
	}
	
	if(list.size() == trackedSize)
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

bool Test::test8()
{
	DoubleLinkedList<int> list;
	bool isPassed = false;
	
	std::cerr << "Test 8: find returns nullptr on empty list:  ";

	if( list.find(42) == nullptr )
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

bool Test::test9()
{
	DoubleLinkedList<int> list;
	bool isPassed = false;

	std::cerr << "Test 9: find returns false when value not in list:  ";

	//add values from 0 to TEST_SIZE-1 inclusively
	for(int i=0; i<TEST_SIZE; i++)
	{
		list.pushFront(i);
	}

	//find value not in list
	if( list.find(-1) == nullptr )
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


bool Test::test10()
{
	DoubleLinkedList<int> list;
	bool isPassed = true;

	std::cerr << "Test 10: find returns point to node when value is in large list:  \n";

	//Add values 0-(TEST_SIZE-1)
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes.  ";
		
		//Add every other node using pushBack
		if( i%2 == 0) 
		{
			list.pushBack(i);
		}
		else
		{
			list.pushFront(i);
		}

		std::cerr.flush();
	}

	//find for all added values. Set flag if any value is not found 
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tfinding " << (i+1) << "/" << TEST_SIZE << " nodes.  "; 
		Node<int>* temp = list.find(i);

		if( temp == nullptr || temp->getValue() != i) 
		{
			isPassed = false;
		}
		std::cerr.flush();
	}

	if(isPassed)
	{
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return (isPassed);
}

bool Test::test11()
{
	DoubleLinkedList<int> list;
	bool isPassed = false;

	redirectOS();
	ss_redirect.clear();
	list.printList();
	restoreOS();

	std::cerr << "Test 10: printList prints empty string for empty list:  ";

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
	DoubleLinkedList<int> list;
	bool isPassed = true;
	int num=0;
	

	std::cerr << "Test 12: printList prints the contents of large list correctly \n";

	//Add values 0-(TEST_SIZE-1)
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes.  ";
		list.pushBack(i);
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
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return (isPassed);
}

bool Test::test13()
{
	DoubleLinkedList<int> list;
	bool isPassed = false;

	std::cerr << "Test 13: removeFront returns false on empty list:  ";

	if( !list.removeFront() ) 
	{
		isPassed = true;
	}

	if(isPassed)
		std::cerr << "PASSED" << std::endl;
	else
		std::cerr << "FAILED" << std::endl;

	return (isPassed);

}


bool Test::test14()
{
	DoubleLinkedList<int> list;
	bool isPassed = false;

	std::cerr << "Test 14: removeBack returns false on empty list:  ";

	if( !list.removeBack() ) 
		isPassed = true;

	if(isPassed)
		std::cerr << "PASSED" << std::endl;
	else
		std::cerr << "FAILED" << std::endl;

	return (isPassed);
}

bool Test::test15()
{
	DoubleLinkedList<int> list;
	bool isPassed = false;
	int trackedSize = 0;

	std::cerr << "Test 15: size preserved by removeFront on populated list: ";

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

			list.pushFront(i);
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
	DoubleLinkedList<int> list;
	bool isPassed = false;
	int trackedSize = 0;

	std::cerr << "Test 16: size preserved by removeBack on populated list: ";

	//Remove back on every 3rd iteration, add otherwise.
	for(int i=0; i<TEST_SIZE; i++)
	{
		if( i>0 && i%3 == 0)
		{

			list.removeBack();
			trackedSize--;
		}
		else
		{

			list.pushBack(i);
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
	DoubleLinkedList<int> list;
	bool isPassed = false;
	int trackedSize = 0;

	std::cerr << "Test 17: size preserved by remove(value) on populated list: ";

	//Remove front on every 3rd iteration, add otherwise.
	for(int i=0; i<TEST_SIZE; i++)
	{
		list.pushBack(i);
		trackedSize++;

	}

	//remove every third value, track the size
	for(int i=0; i<TEST_SIZE; i+=3)
	{
		list.remove(i);
		trackedSize--;
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


bool Test::test18()
{
	DoubleLinkedList<int> list;
	bool isPassed = true;
	int num=0;
	

	std::cerr << "Test 18: order preserved by removeFront on populated list\n ";

	//Add values 0-(TEST_SIZE-1)
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes.  ";
		list.pushBack(i);
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
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return (isPassed);
} 
bool Test::test19()
{
	DoubleLinkedList<int> list;
	bool isPassed = true;
	int num=0;
	

	std::cerr << "Test 19: order preserved by removeBack on populated list\n ";

	//Add values 0-(TEST_SIZE-1)
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes. ";
		list.pushBack(i);
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
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return (isPassed);
}

bool Test::test20()
{
	DoubleLinkedList<int> list;
	bool isPassed = false;

	std::cerr << "Test 20: remove(value) on empty list returns false : ";

	if( !list.remove(42) )
	{
		isPassed = true;
	} 

	if(isPassed)
	{
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return (isPassed);
}

bool Test::test21()
{
	DoubleLinkedList<int> list;
	bool isPassed = false;
	
	std::cerr << "Test 21: remove(value) where value is not in large list returns false\n";

	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes. ";
		list.pushBack(i);
		std::cerr.flush();
	}

	if( !list.remove(-1) )
	{
		isPassed = true;
	}

	if(isPassed)
	{
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return(isPassed);
}

bool Test::test22()
{
	DoubleLinkedList<int> list;
	bool isPassed = true;
	
	std::cerr << "Test 22: remove(value) where value is in large list returns true\n";

	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes. ";
		list.pushBack(i);
		std::cerr.flush();
	}
	
	std::cerr << std::endl;

	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tRemoving " << (i+1) << "/" << TEST_SIZE << " nodes. ";
		if(!list.remove(i))
		{
			isPassed = false;
		}
		std::cerr.flush();
	}

	if(isPassed)
	{
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return(isPassed);

}

bool Test::test23()
{
	DoubleLinkedList<int> list;
	bool isPassed = true;
	int num = 0;

	std::cerr << "Test 23: order preserved by remove(value) on populated list\n";

	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes. ";
		list.pushBack(i);
		std::cerr.flush();
	}
	
	std::cerr << std::endl;

	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tRemoving " << (i+1)/2 << "/" << TEST_SIZE/2 << " nodes. ";
		if(i%2 == 0)
		{
			list.remove(i);
		}
		std::cerr.flush();
	}
	std::cerr << std::endl;

	redirectOS();
	ss_redirect.clear();
	list.printList();
	restoreOS();
	
	int count=1;
	//Check the order of the printed list
	for(int i=1; i<TEST_SIZE; i+=2)
	{
		ss_redirect >> num;
		
		if( i!=num )
		{
			isPassed = false;
		}
		
		std::cerr << '\r' << "\tChecking " << count << "/" << TEST_SIZE/2 << " nodes. ";
		std::cerr.flush();
		count++;
	}

	if(isPassed)
	{
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return(isPassed);

}

bool Test::test24()
{
	DoubleLinkedList<int> list;
	bool isPassed = false;	

	std::cerr << "Test 24: insertAhead on empty list throws exception: ";

	try
	{
		list.insertAhead(0, 1);
	}
	catch(std::exception& e)
	{
		isPassed = true;
	}

	if(isPassed)
	{
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return(isPassed);
}

bool Test::test25()
{
	DoubleLinkedList<int> list;
	bool isPassed = false;	

	std::cerr << "Test 25: insertBehind on empty list throws exception: ";

	try
	{
		list.insertBehind(0, 1);
	}
	catch(std::exception& e)
	{
		isPassed = true;
	}

	if(isPassed)
	{
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return(isPassed);
}


bool Test::test26()
{
	DoubleLinkedList<int> list;
	bool isPassed = false;	

	std::cerr << "Test 26: insertAhead of value not in list throws exception:\n";

	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes. ";
		list.pushBack(i);
		std::cerr.flush();
	}

	try
	{
		list.insertAhead(-1, 1);
	}
	catch(std::exception& e)
	{
		isPassed = true;
	}

	if(isPassed)
	{
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return(isPassed);
}

bool Test::test27()
{
	DoubleLinkedList<int> list;
	bool isPassed = false;	

	std::cerr << "Test 27: insertBehind of value not in list throws exception:\n";

	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tAdding " << (i+1) << "/" << TEST_SIZE << " nodes. ";
		list.pushBack(i);
		std::cerr.flush();
	}

	try
	{
		list.insertBehind(-1, 1);
	}
	catch(std::exception& e)
	{
		isPassed = true;
	}

	if(isPassed)
	{
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return(isPassed);
}

bool Test::test28()
{
	DoubleLinkedList<int> list;
	bool isPassed = false;
	int num1=0, num2=0;

	std::cerr << "Test 28: insertAhead of list size 1 retains list order:";
	list.pushBack(1);


	try
	{
		list.insertAhead(1,0);

		redirectOS();
		ss_redirect.clear();
		list.printList();
		restoreOS();

		ss_redirect >> num1;
		ss_redirect >> num2;

		if(num1 == 0 && num2 == 1)
		{
			isPassed = true;
		}	
	}
	catch(std::exception& e)
	{
		std::cerr << "\nException thrown! ";
		isPassed = false;
	}

	if(isPassed)
	{
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return(isPassed);
}

bool Test::test29()
{
	DoubleLinkedList<int> list;
	bool isPassed = false;
	int num1=0, num2=0;

	std::cerr << "Test 29: insertBehind of list size 1 retains list order:";
	list.pushBack(0);


	try
	{
		list.insertBehind(0,1);

		redirectOS();
		ss_redirect.clear();
		list.printList();
		restoreOS();

		ss_redirect >> num1;
		ss_redirect >> num2;

		if(num1 == 0 && num2 == 1)
		{
			isPassed = true;
		}	
	}
	catch(std::exception& e)
	{
		std::cerr << "\nException thrown! ";
		isPassed = false;
	}

	if(isPassed)
	{
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return(isPassed);
}

bool Test::test30()
{
	DoubleLinkedList<int> list;
	bool isPassed = true;
	bool isExceptionThrown = false;
	int num=0;
	int count=0;

	std::cerr << "Test 30: insertAhead on large list retains list order \n";

	count=1;//keep track of how many nodes are added
	//Add odd numbers from 1 to TEST_SIZE to list
	for(int i=1; i<TEST_SIZE; i+=2)
	{
		std::cerr << '\r' << "\tAdding " << count << "/" << TEST_SIZE/2 << " nodes.";
		list.pushBack(i);
		std::cerr.flush();
		count++;
	}
	std::cout << std::endl;

	count=1;//keep track of how many nodes are added
	//insert even numbers from 0 to TEST_SIZE to list
	for(int i=0; i<TEST_SIZE; i+=2)
	{
		std::cerr << '\r' << "\tInserting " << count << "/" << TEST_SIZE/2 << " nodes.";
		try
		{
			list.insertAhead(i+1, i);
		}
		catch(std::exception& e)
		{
			isExceptionThrown = true;
		}
		std::cerr.flush();
		count++;
	}
	std::cerr << std::endl;
	if(isExceptionThrown)
	{	
		std::cerr << "Exception was thrown during insertion!\n";
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

		std::cerr << '\r' << "\tChecking " << (i+1) << "/" << TEST_SIZE << " nodes. ";
		std::cerr.flush();
	}

	
	isPassed = isPassed && !isExceptionThrown;

	if(isPassed)
	{
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return (isPassed);
}

bool Test::test31()
{
	DoubleLinkedList<int> list;
	bool isPassed = true;
	bool isExceptionThrown = false;
	int num=0;
	int count=0;

	std::cerr << "Test 31: insertBehind on large list retains list order \n";

	count=1;//keep track of how many nodes are added
	//Add even numbers from 0 to TEST_SIZE to list
	for(int i=0; i<TEST_SIZE; i+=2)
	{
		std::cerr << '\r' << "\tAdding " << count << "/" << TEST_SIZE/2 << " nodes.";
		list.pushBack(i);
		std::cerr.flush();
		count++;
	}
	std::cerr << std::endl;

	count=1;//keep track of how many nodes are added
	//insert odd numbers from 1 to TEST_SIZE to list
	for(int i=1; i<TEST_SIZE; i+=2)
	{
		std::cerr << '\r' << "\tInserting " << count << "/" << TEST_SIZE/2 << " nodes.";
		try
		{
			list.insertBehind(i-1, i);
		}
		catch(std::exception& e)
		{
			isExceptionThrown = true;
		}
		std::cerr.flush();
		count++;
	}
	std::cerr << std::endl;

	if(isExceptionThrown)
	{	
		std::cerr << "Exception was thrown during insertion!\n";
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

		std::cerr << '\r' << "\tChecking " << (i+1) << "/" << TEST_SIZE << " nodes. ";
		std::cerr.flush();
	}

	isPassed = isPassed && !isExceptionThrown;

	if(isPassed)
	{
		std::cerr << "PASSED" << std::endl;
	}
	else
	{
		std::cerr << "FAILED" << std::endl;
	}

	return (isPassed);
}
