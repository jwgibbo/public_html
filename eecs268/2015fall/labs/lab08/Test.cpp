#include "Test.h"

void Test::runTests()
{

        int score = 0;

	//Run tests, track total points
        std::cerr << "\n\n=========================\n";
        std::cerr << "   RUNNING TEST SUITE    \n";
        std::cerr << "=========================\n\n";

	score += test_isEmpty01() ? 2 : 0; 	
	score += test_isEmpty02() ? 2 : 0; 

	score += test_search01() ? 2 : 0; 
	score += test_search02() ? 3 : 0;
	score += test_search03() ? 4 : 0;
	score += test_search04() ? 4 : 0;
	score += test_search05() ? 5 : 0;
	score += test_search06() ? 7 : 0;

	score += test_clone01() ? 5 : 0;
	score += test_clone02() ? 7 : 0;

        std::cerr << "\n\n=========================\n";
        std::cerr << "Loading the following into tree for testing:\n";
        std::cerr << "50, 25, 75, 10, 30, 65, 100\n";
        std::cerr << "=========================\n\n";

	score += test_order01() ? 6 : 0;
	score += test_order02() ? 6 : 0;
	score += test_order03() ? 6 : 0;


        std::cerr << "\n\n=========================\n";
        std::cerr << "Tests to verify all values are present:\n";
        std::cerr << "=========================\n\n";

	score += test_order04() ? 7 : 0;
	score += test_order05() ? 7 : 0;
	score += test_order06() ? 7 : 0;


        std::cerr << "\n\n=========================\n";
        std::cerr << "Score: " << score << " / " << MAX_SCORE << "\n";
        std::cerr << "=========================\n" << std::endl;


}


Test::Test() : TEST_SIZE(10000), MAX_SCORE(80)
{
        m_testNum = 0;
}


void Test::printPassFail(bool isPassed) const
{
        if(isPassed)
                std::cerr << "PASSED" << std::endl;
        else
                std::cerr << "FAILED" << std::endl;
}

void Test::printTestMessage(int testNum, std::string testDescription) const
{
        std::cerr << "Test " << testNum << ": " << testDescription << ": ";
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
	std::random_device randomDevice;	
	std::default_random_engine generator(randomDevice());
	std::uniform_int_distribution<int> distribution(0,INT_MAX);
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

void Test::loadVectorIntoTree(const std::vector<int>& vec, BSTI<int>* bst)
{
	for(std::size_t i=0; i<vec.size(); i++)
	{
		bst->add(vec[i]);
	}
}

void Test::printVector(const std::vector<int>& vec)
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

bool Test::test_isEmpty01()
{
	bool isPassed = false;
	BSTI<int>* bst = new BinarySearchTree<int>();
	m_testNum++;

	printTestMessage(m_testNum, "isEmpty returns true on empty tree");

	isPassed = bst->isEmpty();	

	printPassFail(isPassed);
	delete bst;
	return(isPassed);
}

bool Test::test_isEmpty02()
{
	bool isPassed = false;
	BSTI<int>* bst = new BinarySearchTree<int>();
	m_testNum++;

	printTestMessage(m_testNum, "isEmpty returns false after a single add");
	
	bst->add(1);
	isPassed = !bst->isEmpty();	

	printPassFail(isPassed);
	delete bst;
	return(isPassed);
}


bool Test::test_search01()
{
	bool isPassed = false;
	BSTI<int>* bst = new BinarySearchTree<int>();
	m_testNum++;

	printTestMessage(m_testNum, "searching an empty tree returns false");

	isPassed = !bst->search(42);	

	printPassFail(isPassed);
	delete bst;
	return(isPassed);
}

bool Test::test_search02()
{
	bool isPassed = false;
	BSTI<int>* bst = new BinarySearchTree<int>();
	m_testNum++;

	printTestMessage(m_testNum, "add(42) to empty tree then search(42) returns true");

	bst->add(42);
	isPassed = bst->search(42);	

	printPassFail(isPassed);
	delete bst;
	return(isPassed);
}


bool Test::test_search03()
{
	bool isPassed = false;
	BSTI<int>* bst = new BinarySearchTree<int>();
	m_testNum++;

	printTestMessage(m_testNum, "add(42) to right subtree of root of then search(42) returns true");

	bst->add(20);
	bst->add(42);
	isPassed = bst->search(42);	

	printPassFail(isPassed);
	delete bst;
	return(isPassed);
}

bool Test::test_search04()
{
	bool isPassed = false;
	BSTI<int>* bst = new BinarySearchTree<int>();
	m_testNum++;

	printTestMessage(m_testNum, "add(42) to left subtree of root of then search(42) returns true");

	bst->add(100);
	bst->add(42);
	isPassed = bst->search(42);	

	printPassFail(isPassed);
	delete bst;
	return(isPassed);
}

bool Test::test_search05()
{
	bool isPassed = false;
	BSTI<int>* bst = new BinarySearchTree<int>();
	std::vector<int> vec;
	m_testNum++;

	printTestMessage(m_testNum, "searching for a value not in large tree returns false");

	uniqueRandomFill(vec, TEST_SIZE);
	loadVectorIntoTree(vec, bst);
		
	isPassed = !bst->search(-1);	

	printPassFail(isPassed);
	delete bst;
	return(isPassed);
}


bool Test::test_search06()
{
	bool isPassed = true;
	BSTI<int>* bst = new BinarySearchTree<int>();
	std::vector<int> vec;
	m_testNum++;

	printTestMessage(m_testNum, "searching for all values in a large tree of random values; all searches return true");

	uniqueRandomFill(vec, TEST_SIZE);
	loadVectorIntoTree(vec, bst);
		
	for(std::size_t i=0; i<vec.size(); i++)
	{
		if( !bst->search(vec[i])  )
		{
			isPassed = false;	
			std::cerr << "ERROR: Search for " << vec[i] << " returned false after being added." << std::endl;
		}
	}	

	printPassFail(isPassed);
	delete bst;
	return(isPassed);
}

bool Test::test_clone01()
{
	bool isPassed = false;
	BSTI<int>* original = new BinarySearchTree<int>();
	BSTI<int>* copy = nullptr; 
	
	m_testNum++;

	printTestMessage(m_testNum, "cloning an empty tree, deleting original, check that clone is empty");
	copy = original->clone();
	delete original;
	original = nullptr;
	
	isPassed = copy->isEmpty();		

	printPassFail(isPassed);
	delete copy;
	copy = nullptr;
	return(isPassed);
}

bool Test::test_clone02()
{
	bool isPassed = true;
	BSTI<int>* original = new BinarySearchTree<int>();
	BSTI<int>* copy = nullptr; 
	std::vector<int> vec;
	m_testNum++;

	printTestMessage(m_testNum, "cloning a large tree, deleting original, searching for all values in copy");
	
	
	uniqueRandomFill(vec, TEST_SIZE);
	loadVectorIntoTree(vec, original);
		
	copy = original->clone();
	delete original;
	original = nullptr;
	
	for(std::size_t i=0; i<vec.size(); i++)
	{
		if( !copy->search(vec[i])  )
		{
			isPassed = false;	
			std::cerr << "ERROR: Search for " << vec[i] << " returned false after being added." << std::endl;
		}
	}

	printPassFail(isPassed);
	delete copy;
	copy = nullptr;
	return(isPassed);
}


bool Test::test_order01()
{
	bool isPassed = false;
	BSTI<int>* bst = new BinarySearchTree<int>();
	std::vector<int> input = {50, 25, 75, 10, 30, 65, 100}; 
	std::vector<int> correct = {50, 25, 10, 30, 75, 65, 100};
	std::vector<int> output;

	m_testNum++;

	printTestMessage(m_testNum, "vector returned by treeToVector(PRE_ORDER) returns vector: {50, 25, 10, 30, 75, 65, 100}");

	loadVectorIntoTree(input, bst);
	output = bst->treeToVector(PRE_ORDER);

	if(output == correct)
	{
		isPassed = true;
	}
	else
	{
		isPassed = false;
		std::cerr << "ERROR: expected ";
		printVector(correct);
		std::cerr << " got ";
		printVector(output);
		std::cerr << std::endl;	
	}	

	printPassFail(isPassed);

	delete bst;
	return(isPassed);
}

bool Test::test_order02()
{
	bool isPassed = false;
	BSTI<int>* bst = new BinarySearchTree<int>();
	std::vector<int> input = {50, 25, 75, 10, 30, 65, 100}; 
	std::vector<int> correct = {10, 25, 30, 50, 65, 75, 100};
	std::vector<int> output;

	m_testNum++;

	printTestMessage(m_testNum, "vector returned by treeToVector(IN_ORDER) returns vector: {10, 25, 30, 50, 65, 75, 100}");

	loadVectorIntoTree(input, bst);
	output = bst->treeToVector(IN_ORDER);

	if(output == correct)
	{
		isPassed = true;
	}
	else
	{
		isPassed = false;
		std::cerr << "ERROR: expected ";
		printVector(correct);
		std::cerr << " got ";
		printVector(output);
		std::cerr << std::endl;	
	}	

	printPassFail(isPassed);

	delete bst;
	return(isPassed);
}

bool Test::test_order03()
{
	bool isPassed = false;
	BSTI<int>* bst = new BinarySearchTree<int>();
	std::vector<int> input = {50, 25, 75, 10, 30, 65, 100}; 
	std::vector<int> correct = {10, 30, 25, 65, 100, 75, 50};
	std::vector<int> output;

	m_testNum++;

	printTestMessage(m_testNum, "vector returned by treeToVector(IN_ORDER) returns vector: {10, 30, 25, 65, 100, 75, 50}");

	loadVectorIntoTree(input, bst);
	output = bst->treeToVector(POST_ORDER);

	if(output == correct)
	{
		isPassed = true;
	}
	else
	{
		isPassed = false;
		std::cerr << "ERROR: expected ";
		printVector(correct);
		std::cerr << " got ";
		printVector(output);
		std::cerr << std::endl;	
	}	

	printPassFail(isPassed);

	delete bst;
	return(isPassed);
}

bool Test::test_order04()
{
	bool isPassed = true;
	BSTI<int>* bst = new BinarySearchTree<int>();
	std::vector<int> input; 
	std::vector<int> output;

	m_testNum++;

	printTestMessage(m_testNum, "vector returned by treeToVector(PRE_ORDER) returns a vector with all values present in a large tree");
	
	uniqueRandomFill(input, TEST_SIZE);
	loadVectorIntoTree(input, bst);
	output = bst->treeToVector(PRE_ORDER);

	if(input.size() == output.size())
	{
		std::cerr << std::endl;
		for(std::size_t i=0; i<input.size() && isPassed; i++)
		{
			std::cerr << '\r' << "\tVerfiying " << (i+1) << "/" << TEST_SIZE << " nodes.  "; 
			std::cerr.flush();
			if( std::find(output.begin(), output.end(), input[i]) == output.end() )
			{
				isPassed = false;
				std::cerr << "ERROR: " << input[i] << " not present in vector. Test over." << std::endl;
			}
		}
	}
	else
	{
		isPassed = false;
	}

	printPassFail(isPassed);

	delete bst;
	return(isPassed);
}

bool Test::test_order05()
{
	bool isPassed = true;
	BSTI<int>* bst = new BinarySearchTree<int>();
	std::vector<int> input; 
	std::vector<int> output;

	m_testNum++;

	printTestMessage(m_testNum, "vector returned by treeToVector(IN_ORDER) returns a vector with all values present in a large tree");
	
	uniqueRandomFill(input, TEST_SIZE);
	loadVectorIntoTree(input, bst);
	output = bst->treeToVector(IN_ORDER);

	if(input.size() == output.size())
	{
		std::cerr << std::endl;
		for(std::size_t i=0; i<input.size() && isPassed; i++)
		{
			std::cerr << '\r' << "\tVerfiying " << (i+1) << "/" << TEST_SIZE << " nodes.  "; 
			std::cerr.flush();
			if( std::find(output.begin(), output.end(), input[i]) == output.end() )
			{
				isPassed = false;
				std::cerr << "ERROR: " << input[i] << " not present in vector. Test over." << std::endl;
			}
		}
	}
	else
	{
		isPassed = false;
	}

	printPassFail(isPassed);

	delete bst;
	return(isPassed);
}

bool Test::test_order06()
{
	bool isPassed = true;
	BSTI<int>* bst = new BinarySearchTree<int>();
	std::vector<int> input; 
	std::vector<int> output;

	m_testNum++;

	printTestMessage(m_testNum, "vector returned by treeToVector(POST_ORDER) returns a vector with all values present in a large tree");
	
	uniqueRandomFill(input, TEST_SIZE);
	loadVectorIntoTree(input, bst);
	output = bst->treeToVector(POST_ORDER);

	if(input.size() == output.size())
	{
		std::cerr << std::endl;
		for(std::size_t i=0; i<input.size() && isPassed; i++)
		{
			std::cerr << '\r' << "\tVerfiying " << (i+1) << "/" << TEST_SIZE << " nodes.  "; 
			std::cerr.flush();
			if( std::find(output.begin(), output.end(), input[i]) == output.end() )
			{
				isPassed = false;
				std::cerr << "ERROR: " << input[i] << " not present in vector. Test over." << std::endl;
			}
		}
	}
	else
	{
		isPassed = false;
	}

	printPassFail(isPassed);

	delete bst;
	return(isPassed);
}
