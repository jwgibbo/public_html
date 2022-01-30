#include "Test_Stack.h"

void Test_Stack::runTests()
{
	const int MAX_SCORE = 60;
	int score = 0;

	std::cerr << "\n\n=========================\n";
	std::cerr << "   RUNNING TEST SUITE    \n";
	std::cerr << "=========================\n\n";

	//Run test and award points where appropriate
	score += test1() ? 3: 0; 
	score += test2() ? 3: 0; 
	score += test3() ? 4: 0; 
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

Test_Stack::Test_Stack(int testSize) : Test(testSize)
{

}

std::vector<int> Test_Stack::loadValues(Stack<int>& stack)
{
	std::vector<int> vec;

	std::cerr << std::endl;
	for(int i=0; i<TEST_SIZE; i++)
	{
		std::cerr << '\r' << "\tpushing " << (i+1) << "/" << TEST_SIZE << " values.  "; 
		stack.push(i);
		vec.insert(vec.begin(), i);
		std::cerr.flush();
	}

	return(vec);
}

bool Test_Stack::test1()
{
	Stack<int> stack;
	bool isPassed = stack.size() == 0;

	printTestMessage("size of empty stack is zero");
	printPassFail(isPassed);
	return (isPassed);
}


bool Test_Stack::test2()
{
	Stack<int> stack;
	bool isPassed=false;

	stack.push(1);

	printTestMessage("size returns correct value after 1 push");
	isPassed = stack.size() == 1;
	printPassFail(isPassed);	
	return (isPassed);
}




bool Test_Stack::test3()
{
	Stack<int> stack;
	bool isPassed = false;
	printTestMessage("size returns correct value after lots of pushes");
	
	loadValues(stack);
	
	isPassed = stack.size() == TEST_SIZE;

	printPassFail(isPassed);
	return(isPassed);	
}


bool Test_Stack::test4()
{
 	bool isPassed = false;
	Stack<int> stack;

	printTestMessage("peek on empty stack throws PreconditionViolation Exception");

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


bool Test_Stack::test5()
{
	bool isPassed = false;
	Stack<int> stack;
	stack.push(42);
	printTestMessage("peek returns correct value on stack size 1");

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

bool Test_Stack::test6()
{
	Stack<int> stack;
	bool isPassed = false;
	printTestMessage("peek returns correct value after lots of pushes");
	
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


bool Test_Stack::test7()
{
	Stack<int> stack;
	bool isPassed = false;
	printTestMessage("pop on empty stack throws PreconditionViolationException exception");
	

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


bool Test_Stack::test8()
{
	Stack<int> stack;
	bool isPassed = false;
	printTestMessage("pop on stack of size 1 reduces size to zero");
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

bool Test_Stack::test9()
{
	Stack<int> stack;
	bool isPassed = false;
	int trackedSize = 0;
	printTestMessage("size remains accurate after lots of pushes and pops");
	
	try
	{
		for(int i=0; i<TEST_SIZE; i++)
		{
			//pop every fifth iteration
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

bool Test_Stack::test10()
{
	Stack<int> stack;
	bool isPassed = false;
	printTestMessage("toVector on empty Stack creates empty vector");

	
	isPassed = stack.toVector().empty();
	
	printPassFail(isPassed);	
	return(isPassed);
}

bool Test_Stack::test11()
{
	Stack<int> stack;
	std::vector<int> expected, given;
	bool isPassed = false;
	printTestMessage("toVector contains correct values after lots of pushes retains order");

	expected = loadValues(stack);

	isPassed = expected == stack.toVector();		
	printPassFail(isPassed);	
	return(isPassed);
}


bool Test_Stack::test12()
{
	Stack<int> stack;
	bool isPassed = true;	
	std::vector<int> expected, given;

	printTestMessage("toVector after lots of pushes, pops, and peeks retains order");

	expected = loadValues(stack);

	std::cerr << std::endl;	
	//Remove half the stack
	for(int i=0; i<TEST_SIZE/2; i++)
	{
		
		//call peek just to ensure peek does not alter order
		std::cerr << '\r' << "\tpeeking at and popping " << (i+1) << "/" << TEST_SIZE/2 << " values.  "; 
		stack.peek();
		stack.pop();
		expected.erase(expected.begin());
		std::cerr.flush();
	}

	given = stack.toVector();
	isPassed = (expected == given);

	if( !isPassed )
	{
		printExpectedError(expected, given);
	}
	
	printPassFail(isPassed);	
	return(isPassed);
}
