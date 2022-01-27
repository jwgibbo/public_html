#include "Test.h"

void Test::runTests()
{
	
	int score = 0;

	std::cerr << "\n\n=========================\n";
	std::cerr << "   RUNNING TEST SUITE    \n";
	std::cerr << "=========================\n\n";

	//Run test and award points where appropriate
	score += test1() ? 5: 0; 
	score += test2() ? 5: 0; 
	score += test3() ? 5: 0; 
	score += test4() ? 5: 0; 
	score += test5() ? 5: 0; 
	score += test6() ? 5: 0; 
	score += test7() ? 5: 0; 
	score += test8() ? 5: 0; 
	score += test9() ? 5: 0; 
	score += test10() ? 5: 0; 
	score += test11() ? 5: 0; 
	score += test12() ? 10: 0; 

	std::cerr << "Score: " << score << " / " << MAX_SCORE << std::endl;
}


Test::Test(std::ostream& os) : os(os), TEST_SIZE(1000), NUM_TESTS(12), MAX_SCORE(65)
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

void Test::loadValues(Stack<int>& stack)
{
	std::cerr << std::endl;
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tpushing " << (i+1) << "/" << TEST_SIZE << " nodes.  "; 
		stack.push(i);
		std::cerr.flush();
	}
}

void Test::printPassFail(bool isPassed)
{
	if(isPassed)
		std::cerr << "PASSED" << std::endl;
	else
		std::cerr << "FAILED" << std::endl;
}

void Test::printTestMessage(int testNum, std::string testDescription)
{
	std::cerr << "Test " << testNum << ": " << testDescription << ": ";
}

bool Test::test1()
{
	Stack<int> stack;
	bool isPassed = stack.size() == 0;

	printTestMessage(1, "size of empty stack is zero");
	printPassFail(isPassed);
	return (isPassed);
}


bool Test::test2()
{
	Stack<int> stack;
	bool isPassed=false;

	stack.push(1);

	printTestMessage(2, "size returns correct value after 1 push");
	isPassed = stack.size() == 1;
	printPassFail(isPassed);	
	return (isPassed);
}




bool Test::test3()
{
	Stack<int> stack;
	bool isPassed = false;
	printTestMessage(3, "size returns correct value after lots of pushes");
	
	loadValues(stack);
	
	isPassed = stack.size() == TEST_SIZE;

	printPassFail(isPassed);
	return(isPassed);	
}


bool Test::test4()
{
 	bool isPassed = false;
	Stack<int> stack;

	printTestMessage(4, "peek on empty stack throws PreconditionViolation Exception");

	try
	{
		stack.peek();
	}
	catch(PreconditionViolationException& pve)
	{
		isPassed = true;
	}
	catch(...)
	{
		std::cerr << "Unexpected exception thrown!" << std::endl;
	}


	printPassFail(isPassed);
	return (isPassed); 
}


bool Test::test5()
{
	bool isPassed = false;
	Stack<int> stack;
	stack.push(42);
	printTestMessage(5, "peek returns correct value on stack size 1");

	try
	{
		if(stack.peek() == 42)
		{
			isPassed=true;
		}
	}
	catch(...)
	{
		std::cerr << "Unexpected exception thrown!" << std::endl;
	}

	printPassFail(isPassed);
	return (isPassed); 

}

bool Test::test6()
{
	Stack<int> stack;
	bool isPassed = false;
	printTestMessage(6, "peek returns correct value after lots of pushes");
	
	loadValues(stack);
	
	try
	{
		if(stack.peek() == TEST_SIZE-1)
		{
			isPassed=true;
		}
	}
	catch(...)
	{
		std::cerr << "Unexpected exception thrown!" << std::endl;
	}

	printPassFail(isPassed);
	return(isPassed);	
}


bool Test::test7()
{
	Stack<int> stack;
	bool isPassed = false;
	printTestMessage(7, "pop on empty stack throws PreconditionViolationException exception");
	

	try
	{
		stack.pop();
	}
	catch(PreconditionViolationException& pve)
	{
		isPassed = true;
	}
	catch(...)
	{
		std::cerr << "Exception thrown, but not PreconditionViolationException!" << std::endl;
	}

	printPassFail(isPassed);
	return(isPassed);	
}


bool Test::test8()
{
	Stack<int> stack;
	bool isPassed = false;
	printTestMessage(8, "pop on stack of size 1 reduces size to zero");
	stack.push(42);
	
	try
	{
		stack.pop();
		if(stack.size() == 0)
		{
			isPassed = true;
		}
	
	}
	catch(...)
	{
		std::cerr << "Unexpected exception thrown!" << std::endl;
	}	
	
	printPassFail(isPassed);		
	return(isPassed);	
}

bool Test::test9()
{
	Stack<int> stack;
	bool isPassed = false;
	int trackedSize = 0;
	printTestMessage(9, "size remains accurate after lots of pushes and pops");
	
	try
	{
		for(int i=0; i<TEST_SIZE; i++)
		{
			if(i%5 == 0 && i > 0)
			{
				stack.pop();
				trackedSize--;
			}
			else
			{
				stack.push(i);
				trackedSize++;			
			}
		}	
	}
	catch(...)
	{
		std::cerr << "Unexpected exception thrown!" << std::endl;
	}	
	
	isPassed = stack.size() == trackedSize;

	std::cerr << "\nExpected size: " << trackedSize << " size() returned: " << stack.size() << " ";
	printPassFail(isPassed);		
	return(isPassed);	
}

bool Test::test10()
{
	Stack<int> stack;
	bool isPassed = false;
	printTestMessage(10, "print on empty list print empty string");

	redirectOS();
	ss_redirect.clear();
	stack.print();
	restoreOS();

	if(ss_redirect.str().length() == 0)
	{
		isPassed = true;
	}

	printPassFail(isPassed);	
	return(isPassed);
}

bool Test::test11()
{
	Stack<int> stack;
	int num = 0;
	bool isPassed = true;
	printTestMessage(11, "print after lots of pushes retains order");

	loadValues(stack);

	redirectOS();
	ss_redirect.clear();
	stack.print();
	restoreOS();

	//sizes will be printed in reverse, since you know, stacks.
	for(int i=TEST_SIZE-1; i>=0; i--)
	{
		ss_redirect >> num;
		
		if( i!=num )
		{
			isPassed = false;
		}
	}

	printPassFail(isPassed);	
	return(isPassed);
}


bool Test::test12()
{
	Stack<int> stack;
	int num = 0;
	bool isPassed = true;
	printTestMessage(12, "print after lots of pushes, pops, and peeks retains order");

	loadValues(stack);
	
	std::cerr << std::endl;	
	//Remove half the stack
	for(int i=0; i<TEST_SIZE/2; i++)
	{
		
		//call peek just to ensure peek does not alter order
		std::cerr << '\r' << "\tpeeking at and popping " << (i+1) << "/" << TEST_SIZE/2 << " nodes.  "; 
		stack.peek();
		stack.pop();
		std::cerr.flush();
	}

	redirectOS();
	ss_redirect.clear();
	stack.print();
	restoreOS();

	//sizes will be printed in reverse, since you know, stacks.
	for(int i=(TEST_SIZE/2)-1; i>=0; i--)
	{
		ss_redirect >> num;
		
		if( i!=num )
		{
			isPassed = false;
		}
	}
	
	printPassFail(isPassed);	
	return(isPassed);
}
