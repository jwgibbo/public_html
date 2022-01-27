#include "Test.h"

void Test::runTests()
{
	
	int score = 0;

	std::cerr << "\n\n=========================\n";
	std::cerr << "   RUNNING TEST SUITE    \n";
	std::cerr << "=========================\n\n";

	//Run test and award points where appropriate
	score += test1() ? 3: 0; 
	score += test2() ? 4: 0; 
	score += test3() ? 3: 0; 
	score += test4() ? 3: 0; 
	score += test5() ? 3: 0; 
	score += test6() ? 3: 0; 
	score += test7() ? 3: 0; 
	score += test8() ? 3: 0; 
	score += test9() ? 3: 0; 
	score += test10() ? 3: 0; 
	score += test11() ? 10: 0; 
	score += test12() ? 10: 0;
	score += test13() ? 10: 0; 
	score += test14() ? 10: 0; 
	score += test15() ? 3 : 0;
	score += test16() ? 3 : 0;
	score += test17() ? 3 : 0;


	std::cerr << "Score: " << score << " / " << MAX_SCORE << std::endl;
}


Test::Test(std::ostream& os) : os(os), TEST_SIZE(10000), NUM_TESTS(12), MAX_SCORE(80)
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
	bool isPassed = true; //this test will most likely cause a segfault, so we'll assume true 
	const int SIZE = 66;
	printTestMessage(1, "createTestArray creates an array of the requested size");
	
	int* arr = Sorts<int>::createTestArray(SIZE, 1, 1);
	
	//attempt access all elements in the array
	for(int i=0; i<SIZE; i++)
	{
		arr[i]= -1;
	}
	
	delete[] arr;
	arr = nullptr;
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test2()
{
	bool isPassed = true;
	const int SIZE = 1000;
	const int LOW = -100;
	const int HIGH = 100;
	int* arr = Sorts<int>::createTestArray(SIZE, LOW, HIGH);

	printTestMessage(2, "createTestArray creates an array with values in the provided range");
	
	//check each value to ensure it's in range
	for(int i=0; i<SIZE && isPassed; i++)
	{
		if(arr[i] < LOW || arr[i] > HIGH)
		{
			isPassed = false;
			std::cerr << "ERROR! Excepted value from " << LOW << " to " << HIGH << ". Got " << arr[i];
			std::cerr << std::endl;
		}
	}
	
	delete[] arr;
	arr = nullptr;
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test3()
{
	bool isPassed = false;
	int* arr = nullptr;

	printTestMessage(3, "isSorted returns true when array size is 1");
	

	isPassed = Sorts<int>::isSorted(arr, 1);
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test4()
{
	bool isPassed = false;
	int arr[] = {31, 1, 0, 4, 1};

	printTestMessage(4, "isSorted returns false when array is not sorted");
	
	isPassed = Sorts<int>::isSorted(arr, 5) == false;
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test5()
{
	bool isPassed = false;
	int arr[] = {31,30,29,28,27};

	printTestMessage(5, "isSorted returns false when array is sorted, but not ascending");
	
	isPassed = Sorts<int>::isSorted(arr, 5) == false;
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test6()
{
	bool isPassed = false;
	int arr[] = {27,27,29,64,65};

	printTestMessage(6, "isSorted returns true when array is sorted in ascending order");
	
	isPassed = Sorts<int>::isSorted(arr, 5);
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test7()
{
	bool isPassed = false;
	int arr[] = {27};

	printTestMessage(7, "bubble sort called with an array of size 1");
	
	Sorts<int>::bubbleSort(arr, 1);
	isPassed = Sorts<int>::isSorted(arr,1);
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test8()
{
	bool isPassed = false;
	int arr[] = {27};

	printTestMessage(8, "insertion sort called with an array of size 1");
	
	Sorts<int>::insertionSort(arr, 1);
	isPassed = Sorts<int>::isSorted(arr,1);
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test9()
{
	bool isPassed = false;
	int arr[] = {27};

	printTestMessage(9, "selection sort called with an array of size 1");
	
	Sorts<int>::insertionSort(arr, 1);
	isPassed = Sorts<int>::isSorted(arr,1);
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test10()
{
	bool isPassed = false;
	int arr[] = {27};

	printTestMessage(10, "bogo sort called with an array of size 1");
	
	Sorts<int>::insertionSort(arr, 1);
	isPassed = Sorts<int>::isSorted(arr,1);
	
	printPassFail(isPassed);
	return (isPassed);
}
/*
bool test11(); //bubble sort sorts an array of size n in ascending order
bool test12(); //inserstion sort sorts an array of size n in ascending order
bool test13(); //selection sort sorts an array of size n in ascending order
bool test14(); //bogo sort sorts an array of size 7 in ascending order
*/
bool Test::test11()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);

	printTestMessage(11, "bubble sort called with an array of size " + std::to_string(TEST_SIZE));
	
	Sorts<int>::bubbleSort(arr, TEST_SIZE);
	isPassed = Sorts<int>::isSorted(arr, TEST_SIZE);
	
	delete[] arr;
	arr = nullptr;

	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test12()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);

	printTestMessage(12, "insertion sort called with an array of size " + std::to_string(TEST_SIZE));
	
	Sorts<int>::insertionSort(arr, TEST_SIZE);
	isPassed = Sorts<int>::isSorted(arr, TEST_SIZE);
	
	delete[] arr;
	arr = nullptr;

	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test13()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);

	printTestMessage(13, "selection sort called with an array of size " + std::to_string(TEST_SIZE));
	
	Sorts<int>::selectionSort(arr, TEST_SIZE);
	isPassed = Sorts<int>::isSorted(arr, TEST_SIZE);
	
	delete[] arr;
	arr = nullptr;

	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test14()
{
	bool isPassed = false;
	const int SIZE = 8;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(SIZE, LOW, HIGH);

	printTestMessage(14, "bogo sort called with an array of size " + std::to_string(SIZE));
	
	Sorts<int>::bogoSort(arr, SIZE);
	isPassed = Sorts<int>::isSorted(arr, SIZE);
	
	delete[] arr;
	arr = nullptr;

	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test15()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);
	double time = 0.0;

	printTestMessage(15, "bubble sort completes in reasonable amount of time (0-10secs platform dependent) " + std::to_string(TEST_SIZE));
	
	time = Sorts<int>::sortTimer(Sorts<int>::bubbleSort, arr, TEST_SIZE);
	
	std::cerr << "\nTime for bubble sort on " + std::to_string(TEST_SIZE) + " elements: " << time << " ";	
	
	if(time<0 || time>10)
	{
		isPassed = false;
	}
	else
	{
		isPassed = true;
	}
	
	delete[] arr;
	arr = nullptr;

	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test16()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);
	double time = 0.0;

	printTestMessage(16, "insertion sort completes in reasonable amount of time (0-10secs platform dependent) " + std::to_string(TEST_SIZE));
	
	time = Sorts<int>::sortTimer(Sorts<int>::insertionSort, arr, TEST_SIZE);
	
	std::cerr << "\nTime for insertion sort on " + std::to_string(TEST_SIZE) + " elements: " << time << " ";	
	
	if(time<0 || time>10)
	{
		isPassed = false;
	}
	else
	{
		isPassed = true;
	}
	
	delete[] arr;
	arr = nullptr;

	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test17()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);
	double time = 0.0;

	printTestMessage(17, "selection sort completes in reasonable amount of time (0-10secs platform dependent) " + std::to_string(TEST_SIZE));
	
	time = Sorts<int>::sortTimer(Sorts<int>::selectionSort, arr, TEST_SIZE);
	
	std::cerr << "\nTime for selection sort on " + std::to_string(TEST_SIZE) + " elements: " << time << " ";	
	
	if(time<0 || time>10)
	{
		isPassed = false;
	}
	else
	{
		isPassed = true;
	}
	
	delete[] arr;
	arr = nullptr;

	printPassFail(isPassed);
	return (isPassed);
}
