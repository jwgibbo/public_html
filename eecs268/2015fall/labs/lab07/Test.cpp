#include "Test.h"

void Test::runTests()
{
	
	int score = 0;

	std::cerr << "\n\n=========================\n";
	std::cerr << "   RUNNING TEST SUITE    \n";
	std::cerr << "=========================\n\n";

	//Run test and award points where appropriate
	std::cerr << "\n\n=========================\n";
	std::cerr << "   SORTS TESTS    \n";
	std::cerr << "=========================\n\n";
	//Sort tests
	score += test_sort1() ? 1: 0; 
	score += test_sort2() ? 1: 0; 
	score += test_sort3() ? 1: 0; 
	score += test_sort4() ? 1: 0; 
	score += test_sort5() ? 1: 0; 
	score += test_sort6() ? 1: 0; 
	score += test_sort7() ? 1: 0; 
	score += test_sort8() ? 1: 0; 
	score += test_sort9() ? 1: 0; 
	score += test_sort10() ? 1: 0; 
	score += test_sort11() ? 1: 0; 
	score += test_sort12() ? 1: 0;
	score += test_sort13() ? 1: 0; 
	score += test_sort14() ? 1: 0; 
	score += test_sort15() ? 1 : 0;
	score += test_sort16() ? 1 : 0;
	score += test_sort17() ? 2 : 0;
	score += test_sort18() ? 2: 0; 
	score += test_sort19() ? 2: 0; 
	score += test_sort20() ? 2: 0; 
	score += test_sort21() ? 3: 0; 
	score += test_sort22() ? 3: 0; 
	score += test_sort23() ? 3: 0; 
	score += test_sort24() ? 3: 0; 
	score += test_sort25() ? 3: 0; 
	score += test_sort26() ? 3: 0; 


	std::cerr << "\n\n=========================\n";
	std::cerr << "   NUMBER FILE GENERATOR TESTS    \n";
	std::cerr << "=========================\n\n";
	
	//Number file generator tests
	score += test_NumFileGen1() ? 3: 0;
	score += test_NumFileGen2() ? 3: 0;
	score += test_NumFileGen3() ? 3: 0;
	score += test_NumFileGen4() ? 3: 0;
	score += test_NumFileGen5() ? 3: 0;
	score += test_NumFileGen6() ? 3: 0;
	
	
	std::cerr << "\n\n=========================\n";
	std::cerr << "   NUMBER FILE DRIVER TESTS    \n";
	std::cerr << "=========================\n\n";

	score += test_NumFileDriver1() ? 2: 0;
	score += test_NumFileDriver2() ? 2: 0;
	score += test_NumFileDriver3() ? 2: 0;
	score += test_NumFileDriver4() ? 2: 0;

	std::cerr << "\n\n=========================\n";
	std::cerr << "   SORT FILE DRIVER TESTS    \n";
	std::cerr << "=========================\n\n";
	score += test_SortDriver1() ? 2: 0;
	score += test_SortDriver2() ? 2: 0;
	score += test_SortDriver3() ? 2: 0;
	score += test_SortDriver4() ? 2: 0;
	score += test_SortDriver5() ? 2: 0;
	score += test_SortDriver6() ? 2: 0;

	std::cerr << "Score: " << score << " / " << MAX_SCORE << std::endl;
}


Test::Test(std::ostream& os) : os(os), TEST_SIZE(10000), MAX_SCORE(80)
{
	m_testNum = 0;
}


void Test::redirectOS()
{
	os_rdbuf = os.rdbuf(ss_redirect.rdbuf());
}


void Test::restoreOS()
{
	os.rdbuf(os_rdbuf);
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

bool Test::isFileAccessible(std::string fileName) const
{
	std::ifstream file(fileName);
	bool isFileGood = file.good();
	file.close();
	return( isFileGood );
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

bool Test::test_sort1()
{
	bool isPassed = true; //this test will most likely cause a segfault, so we'll assume true 
	const int SIZE = 66;
	
	m_testNum++;
	printTestMessage(m_testNum, "createTestArray creates an array of the requested size");
	
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

bool Test::test_sort2()
{
	bool isPassed = true;
	const int SIZE = 1000;
	const int LOW = -100;
	const int HIGH = 100;
	int* arr = Sorts<int>::createTestArray(SIZE, LOW, HIGH);

	m_testNum++;
	printTestMessage(m_testNum, "createTestArray creates an array with values in the provided range");
	
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

bool Test::test_sort3()
{
	bool isPassed = false;
	int* arr = nullptr;

	m_testNum++;
	printTestMessage(m_testNum, "isSorted returns true when array size is 1");
	

	isPassed = Sorts<int>::isSorted(arr, 1);
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_sort4()
{
	bool isPassed = false;
	int arr[] = {31, 1, 0, 4, 1};

	m_testNum++;
	printTestMessage(m_testNum, "isSorted returns false when array is not sorted");
	
	isPassed = Sorts<int>::isSorted(arr, 5) == false;
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_sort5()
{
	bool isPassed = false;
	int arr[] = {31,30,29,28,27};


	m_testNum++;
	printTestMessage(m_testNum, "isSorted returns false when array is sorted, but not ascending");
	
	isPassed = Sorts<int>::isSorted(arr, 5) == false;
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_sort6()
{
	bool isPassed = false;
	int arr[] = {27,27,29,64,65};

	m_testNum++;
	printTestMessage(m_testNum, "isSorted returns true when array is sorted in ascending order");
	
	isPassed = Sorts<int>::isSorted(arr, 5);
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_sort7()
{
	bool isPassed = false;
	int arr[] = {27};

	m_testNum++;
	printTestMessage(m_testNum, "bubble sort called with an array of size 1");
	
	Sorts<int>::bubbleSort(arr, 1);
	isPassed = Sorts<int>::isSorted(arr,1);
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_sort8()
{
	bool isPassed = false;
	int arr[] = {27};

	m_testNum++;
	printTestMessage(m_testNum, "insertion sort called with an array of size 1");
	
	Sorts<int>::insertionSort(arr, 1);
	isPassed = Sorts<int>::isSorted(arr,1);
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_sort9()
{
	bool isPassed = false;
	int arr[] = {27};

	m_testNum++;
	printTestMessage(m_testNum, "selection sort called with an array of size 1");
	
	Sorts<int>::insertionSort(arr, 1);
	isPassed = Sorts<int>::isSorted(arr,1);
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_sort10()
{
	bool isPassed = false;
	int arr[] = {27};

	m_testNum++;
	printTestMessage(m_testNum, "bogo sort called with an array of size 1");
	
	Sorts<int>::bogoSort(arr, 1);
	isPassed = Sorts<int>::isSorted(arr,1);
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_sort11()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);

	m_testNum++;
	printTestMessage(m_testNum, "bubble sort called with an array of size " + std::to_string(TEST_SIZE));
	
	Sorts<int>::bubbleSort(arr, TEST_SIZE);
	isPassed = Sorts<int>::isSorted(arr, TEST_SIZE);
	
	delete[] arr;
	arr = nullptr;

	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_sort12()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);

	m_testNum++;
	printTestMessage(m_testNum, "insertion sort called with an array of size " + std::to_string(TEST_SIZE));
	
	Sorts<int>::insertionSort(arr, TEST_SIZE);
	isPassed = Sorts<int>::isSorted(arr, TEST_SIZE);
	
	delete[] arr;
	arr = nullptr;

	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_sort13()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);

	m_testNum++;
	printTestMessage(m_testNum, "selection sort called with an array of size " + std::to_string(TEST_SIZE));
	
	Sorts<int>::selectionSort(arr, TEST_SIZE);
	isPassed = Sorts<int>::isSorted(arr, TEST_SIZE);
	
	delete[] arr;
	arr = nullptr;

	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_sort14()
{
	bool isPassed = false;
	const int SIZE = 4;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(SIZE, LOW, HIGH);

	m_testNum++;
	printTestMessage(m_testNum, "bogo sort called with an array of size " + std::to_string(SIZE));
	
	Sorts<int>::bogoSort(arr, SIZE);
	isPassed = Sorts<int>::isSorted(arr, SIZE);
	
	delete[] arr;
	arr = nullptr;

	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_sort15()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);
	double time = 0.0;

	m_testNum++;
	printTestMessage(m_testNum, "bubble sort completes in reasonable amount of time (0-10secs platform dependent) " + std::to_string(TEST_SIZE));
	
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

bool Test::test_sort16()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);
	double time = 0.0;

	m_testNum++;
	printTestMessage(m_testNum, "insertion sort completes in reasonable amount of time (0-10secs platform dependent) " + std::to_string(TEST_SIZE));
	
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

bool Test::test_sort17()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);
	double time = 0.0;

	m_testNum++;
	printTestMessage(m_testNum, "selection sort completes in reasonable amount of time (0-10secs platform dependent) " + std::to_string(TEST_SIZE));
	
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

bool Test::test_sort18()
{
	bool isPassed = false;
	int arr[] = {27};

	m_testNum++;
	printTestMessage(m_testNum, "merge sort called with an array of size 1");
	
	Sorts<int>::mergeSort(arr, 1);
	isPassed = Sorts<int>::isSorted(arr,1);
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_sort19()
{
	bool isPassed = false;
	int arr[] = {27};

	m_testNum++;
	printTestMessage(m_testNum, "quick sort called with an array of size 1");
	
	Sorts<int>::quickSort(arr, 1);
	isPassed = Sorts<int>::isSorted(arr,1);
	
	printPassFail(isPassed);
	return (isPassed);
}


bool Test::test_sort20()
{
	bool isPassed = false;
	int arr[] = {27};

	m_testNum++;
	printTestMessage(m_testNum, "quickSortWithMedian sort called with an array of size 1");
	
	Sorts<int>::quickSortWithMedian(arr, 1);
	isPassed = Sorts<int>::isSorted(arr,1);
	
	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_sort21()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);

	m_testNum++;
	printTestMessage(m_testNum, "merge sort called with an array of size " + std::to_string(TEST_SIZE));
	
	Sorts<int>::mergeSort(arr, TEST_SIZE);
	isPassed = Sorts<int>::isSorted(arr, TEST_SIZE);
	
	delete[] arr;
	arr = nullptr;

	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_sort22()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);

	m_testNum++;
	printTestMessage(m_testNum, "quick sort called with an array of size " + std::to_string(TEST_SIZE));
	
        Sorts<int>::quickSort(arr, TEST_SIZE);
	isPassed = Sorts<int>::isSorted(arr, TEST_SIZE);
	
	delete[] arr;
	arr = nullptr;

	printPassFail(isPassed);
	return (isPassed);
}


bool Test::test_sort23()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);

	m_testNum++;
	printTestMessage(m_testNum, "quickSortWithMedian sort called with an array of size " + std::to_string(TEST_SIZE));
	
        Sorts<int>::quickSortWithMedian(arr, TEST_SIZE);
	isPassed = Sorts<int>::isSorted(arr, TEST_SIZE);
	
	delete[] arr;
	arr = nullptr;

	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_sort24()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);
	double time = 0.0;

	m_testNum++;
	printTestMessage(m_testNum, "merge sort completes in reasonable amount of time (0-2secs platform dependent) " + std::to_string(TEST_SIZE));
	
	time = Sorts<int>::sortTimer(Sorts<int>::mergeSort, arr, TEST_SIZE);
	
	std::cerr << "\nTime for merge sort on " + std::to_string(TEST_SIZE) + " elements: " << time << " ";	
	
	if(time<0 || time>2)
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

bool Test::test_sort25()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);
	double time = 0.0;

	m_testNum++;
	printTestMessage(m_testNum, "quick sort completes in reasonable amount of time (0-2secs platform dependent) " + std::to_string(TEST_SIZE));
	
	time = Sorts<int>::sortTimer(Sorts<int>::quickSort, arr, TEST_SIZE);
	
	std::cerr << "\nTime for quick sort on " + std::to_string(TEST_SIZE) + " elements: " << time << " ";	
	
	if(time<0 || time>2)
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

bool Test::test_sort26()
{
	bool isPassed = false;
	const int LOW = 0;
	const int HIGH = 5000;
	int* arr = Sorts<int>::createTestArray(TEST_SIZE, LOW, HIGH);
	double time = 0.0;

	m_testNum++;
	printTestMessage(m_testNum, "quickSortWithMedian sort completes in reasonable amount of time (0-2secs platform dependent) " + std::to_string(TEST_SIZE));
	
	time = Sorts<int>::sortTimer(Sorts<int>::quickSortWithMedian, arr, TEST_SIZE);
	
	std::cerr << "\nTime for quickSortWithMedian sort on " + std::to_string(TEST_SIZE) + " elements: " << time << " ";	
	
	if(time<0 || time>2)
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

bool Test::test_NumFileGen1()
{
	bool isPassed = true;

	std::string ascendingFileName = "test_ascending.dat";
	std::string descendingFileName = "test_descending.dat";
	std::string randomFileName = "test_random.dat";
	std::string singleValueFileName = "test_single.dat";

	const int LOW = 0;
	const int HIGH = 5000;
	const int AMOUNT = 10;
	const int SINGLE_VALUE = 27; 

	m_testNum++;
	printTestMessage(m_testNum, "all files creation methods create file of desired name");
	
	NumberFileGenerator::ascending(ascendingFileName, AMOUNT);
	NumberFileGenerator::descending(descendingFileName, AMOUNT);
	NumberFileGenerator::random(randomFileName, AMOUNT, LOW, HIGH);
	NumberFileGenerator::singleValue(singleValueFileName, AMOUNT, SINGLE_VALUE);

	if(!isFileAccessible(ascendingFileName))
	{
		std::cerr << "ERROR: " << ascendingFileName << " not accessible!" << std::endl;
		isPassed = false;
	}	

	if(!isFileAccessible(ascendingFileName))
	{
		std::cerr << "ERROR: " << descendingFileName << " not accessible!" << std::endl;
		isPassed = false;
	}	

	if(!isFileAccessible(ascendingFileName))
	{
		std::cerr << "ERROR: " << randomFileName << " not accessible!" << std::endl;
		isPassed = false;
	}	

	if(!isFileAccessible(ascendingFileName))
	{
		std::cerr << "ERROR: " << singleValueFileName << " not accessible!" << std::endl;
		isPassed = false;
	}	

	printPassFail(isPassed);
	return (isPassed);
}

bool Test::test_NumFileGen2()
{
	bool isPassed = true;

	std::string ascendingFileName = "test_ascending.dat";
	std::string descendingFileName = "test_descending.dat";
	std::string randomFileName = "test_random.dat";
	std::string singleValueFileName = "test_single.dat";

	std::ifstream ascendingFile(ascendingFileName);
	std::ifstream descendingFile(descendingFileName);
	std::ifstream randomFile(randomFileName);
	std::ifstream singleValueFile(singleValueFileName);

	const int LOW = 0;
	const int HIGH = 5000;
	const int AMOUNT = 100;
	const int SINGLE_VALUE = 28; 

	
	int fileAmount=0; //value read in from file

	m_testNum++;
	printTestMessage(m_testNum, "all files creation methods place the number of values written at top of file");
	
	NumberFileGenerator::ascending(ascendingFileName, AMOUNT);
	NumberFileGenerator::descending(descendingFileName, AMOUNT);
	NumberFileGenerator::random(randomFileName, AMOUNT, LOW, HIGH);
	NumberFileGenerator::singleValue(singleValueFileName, AMOUNT, SINGLE_VALUE);

	
	ascendingFile >> fileAmount;	
	if(fileAmount != AMOUNT)
	{
		std::cerr << "ERROR: expecting " << AMOUNT << " got " << fileAmount
 		          << " in " << ascendingFileName << std::endl;
		isPassed = false;
	}	
	
	
	descendingFile >> fileAmount;	
	if(fileAmount != AMOUNT)
	{
		std::cerr << "ERROR: expecting " << AMOUNT << " got " << fileAmount
 		          << " in " << descendingFileName << std::endl;
		isPassed = false;
	}

	randomFile >> fileAmount;	
	if(fileAmount != AMOUNT)
	{
		std::cerr << "ERROR: expecting " << AMOUNT << " got " << fileAmount
 		          << " in " << randomFileName << std::endl;
		isPassed = false;
	}

	singleValueFile >> fileAmount;	
	if(fileAmount != AMOUNT)
	{
		std::cerr << "ERROR: expecting " << AMOUNT << " got " << fileAmount
 		          << " in " << singleValueFileName << std::endl;
		isPassed = false;
	}

	printPassFail(isPassed);

	ascendingFile.close();
	descendingFile.close();
	randomFile.close();
	singleValueFile.close();

	return (isPassed);
}

bool Test::test_NumFileGen3()
{
	bool isPassed = false;
	const int AMOUNT = 10;
	std::string ascendingFileName = "test_ascending.dat";
	std::ifstream ascendingFile(ascendingFileName);
	std::size_t fileAmount = 0;
	int temp = 0;
	std::vector<int> nums;
	
	NumberFileGenerator::ascending(ascendingFileName, AMOUNT);

	m_testNum++;
	printTestMessage(m_testNum, "ascending method creates files with numbers in ascending order");
	
	ascendingFile >> fileAmount;
	while(!ascendingFile.eof())
	{
		ascendingFile >> temp;
		nums.push_back(temp);
	}
	
	isPassed = isSortedAscending(nums);

	if(fileAmount != nums.size())
	{
		std::cerr << "ERROR: " << fileAmount << " value excepted in file, " 
				<< nums.size() << " read. Is there a newline after last number?" << std::endl;
		isPassed = false;
	}

	printPassFail(isPassed);

	ascendingFile.close();
	return (isPassed);
}

bool Test::test_NumFileGen4()
{
	bool isPassed = false;
	const int AMOUNT = 100;
	std::string descendingFileName = "test_descending.dat";
	std::ifstream descendingFile(descendingFileName);
	std::size_t fileAmount = 0;
	int temp = 0;
	std::vector<int> nums;
	
	NumberFileGenerator::descending(descendingFileName, AMOUNT);

	m_testNum++;
	printTestMessage(m_testNum, "descending method creates files with numbers in descending order");
	
	descendingFile >> fileAmount;
	while(!descendingFile.eof())
	{
		descendingFile >> temp;
		nums.push_back(temp);
	}
	
	isPassed = isSortedDescending(nums);

	if(fileAmount != nums.size())
	{
		std::cerr << "ERROR: " << fileAmount << " value excepted in file, " 
				<< nums.size() << " read. Is there a newline after last number?" << std::endl;
		isPassed = false;
	}	

	printPassFail(isPassed);

	descendingFile.close();
	return (isPassed);
}

bool Test::test_NumFileGen5()
{
	bool isPassed = false;
	const int AMOUNT = 100;
	const int LOW = 0;
	const int HIGH = 5000;

	std::string randomFileName = "test_random.dat";
	std::ifstream randomFile(randomFileName);
	std::size_t fileAmount = 0;
	int temp = 0;
	std::vector<int> nums;
	
	NumberFileGenerator::random(randomFileName, AMOUNT, LOW, HIGH);

	m_testNum++;
	printTestMessage(m_testNum, "random method creates files with numbers in random order");
	
	randomFile >> fileAmount;
	while(!randomFile.eof())
	{
		randomFile >> temp;
		nums.push_back(temp);
	}
	
	//should not be sorted, though there is a very small chance it could
	isPassed = (!isSortedDescending(nums) && !isSortedAscending(nums));

	if(!isPassed) 
	{
		std::cerr << "ERROR: File does not appear to be random. Check manually." << std::endl;
	}

	if(fileAmount != nums.size())
	{
		std::cerr << "ERROR: " << fileAmount << " value excepted in file, " 
				<< nums.size() << " read. Is there a newline after last number?" << std::endl;
		isPassed = false;
	}

	printPassFail(isPassed);

	randomFile.close();
	return (isPassed);
}

bool Test::test_NumFileGen6()
{
	bool isPassed = true;
	const int AMOUNT = 100;
	const int VALUE = 31;
	std::string singleValueFileName = "test_single.dat";
	std::ifstream singleValueFile(singleValueFileName);
	std::size_t fileAmount = 0;
	int temp = 0;
	std::vector<int> nums;
	
	NumberFileGenerator::singleValue(singleValueFileName, AMOUNT, VALUE);

	m_testNum++;
	printTestMessage(m_testNum, "single method creates file with a single value repeated");
	
	singleValueFile >> fileAmount;
	while(!singleValueFile.eof())
	{
		singleValueFile >> temp;
		nums.push_back(temp);
		if(temp != VALUE)
		{
			isPassed = false;
		}
	}

	if(fileAmount != nums.size())
	{
		std::cerr << "ERROR: " << fileAmount << " value excepted in file, " 
				<< nums.size() << " read. Is there a newline after last number?" << std::endl;
		isPassed = false;
	}

	printPassFail(isPassed);

	singleValueFile.close();
	return (isPassed);
}

bool Test::test_NumFileDriver1()
{
	bool isPassed = false;

	std::string fileName = "test_ascending.dat";
	std::ifstream file;
	std::size_t fileAmount = 0;
	int temp = 0;
	std::vector<int> nums;
	const int argc = 5;
	const int AMOUNT = 100;

	char* argv[argc];
	argv[0] = (char*)"./SortingSuite";
	argv[1] = (char*)"-create";
	argv[2] = (char*)"-a";
	argv[3] = (char*)fileName.c_str();
	argv[4] = (char*)"100";

	
	m_testNum++;
	printTestMessage(m_testNum, "Testing for Number Driver \"./prog -create -a " + fileName + " " + std::to_string(AMOUNT) + "\". Driver output below\n");
	
	NumberFileDriver::run(argc, argv);

	if(isFileAccessible(fileName))
	{
		file.open(fileName);

		file >> fileAmount;
		while(!file.eof())
		{
			file >> temp;
			nums.push_back(temp);
		}
	
		isPassed = isSortedAscending(nums);

		if(fileAmount != nums.size())
		{
			std::cerr << "ERROR: " << fileAmount << " value excepted in file, " 
					<< nums.size() << " read. Is there a newline after last number?" << std::endl;
			isPassed = false;
		}
	}
	else
	{
		std::cerr << "ERROR: " << fileName << " not accessible!" << std::endl;
	}

	printPassFail(isPassed);

	file.close();
	return (isPassed);
}


bool Test::test_NumFileDriver2()
{
	bool isPassed = false;

	std::string fileName = "test_descending.dat";
	std::ifstream file;
	std::size_t fileAmount = 0;
	int temp = 0;
	std::vector<int> nums;
	const int argc = 5;
	const int AMOUNT = 100;

	char* argv[argc];
	argv[0] = (char*)"./SortingSuite";
	argv[1] = (char*)"-create";
	argv[2] = (char*)"-d";
	argv[3] = (char*)fileName.c_str();
	argv[4] = (char*)"100";

	
	m_testNum++;
	printTestMessage(m_testNum, "Testing for Number Driver \"./prog -create -d " + fileName + " " + std::to_string(AMOUNT) + "\". Driver output below\n");
	
	NumberFileDriver::run(argc, argv);

	if(isFileAccessible(fileName))
	{
		file.open(fileName);

		file >> fileAmount;
		while(!file.eof())
		{
			file >> temp;
			nums.push_back(temp);
		}
	
		isPassed = isSortedDescending(nums);

		if(fileAmount != nums.size())
		{
			std::cerr << "ERROR: " << fileAmount << " value excepted in file, " 
					<< nums.size() << " read. Is there a newline after last number?" << std::endl;
			isPassed = false;
		}
	}
	else
	{
		std::cerr << "ERROR: " << fileName << " not accessible!" << std::endl;
	}

	printPassFail(isPassed);

	file.close();
	return (isPassed);
}

bool Test::test_NumFileDriver3()
{
	bool isPassed = false;

	std::string fileName = "test_random.dat";
	std::ifstream file;
	std::size_t fileAmount = 0;
	int temp = 0;
	std::vector<int> nums;
	const int argc = 7;
	const int AMOUNT = 100;
	const int LOW = 0;
	const int HIGH = 5000;

	char* argv[argc];
	argv[0] = (char*)"./SortingSuite";
	argv[1] = (char*)"-create";
	argv[2] = (char*)"-r";
	argv[3] = (char*)fileName.c_str();
	argv[4] = (char*)"100";
	argv[5] = (char*)"0";
	argv[6] = (char*)"5000";

	
	m_testNum++;
	printTestMessage(m_testNum, "Testing for Number Driver \"./prog -create -r " + fileName + " " + std::to_string(AMOUNT) + " " + std::to_string(LOW) + " " + std::to_string(HIGH) + "\". Driver output below\n");
	
	NumberFileDriver::run(argc, argv);

	if(isFileAccessible(fileName))
	{
		file.open(fileName);

		file >> fileAmount;
		while(!file.eof())
		{
			file >> temp;
			nums.push_back(temp);
		}
	
		isPassed = !isSortedDescending(nums) && !isSortedAscending(nums);

		if(fileAmount != nums.size())
		{
			std::cerr << "ERROR: " << fileAmount << " value excepted in file, " 
					<< nums.size() << " read. Is there a newline after last number?" << std::endl;
			isPassed = false;
		}
	}
	else
	{
		std::cerr << "ERROR: " << fileName << " not accessible!" << std::endl;
	}

	printPassFail(isPassed);

	file.close();
	return (isPassed);
}

bool Test::test_NumFileDriver4()
{
	bool isPassed = true;

	std::string fileName = "test_singleValue.dat";
	std::ifstream file;
	std::size_t fileAmount = 0;
	int temp = 0;
	std::vector<int> nums;
	const int argc = 6;
	const int AMOUNT = 100;
	const int VALUE = 42;

	char* argv[argc];
	argv[0] = (char*)"./SortingSuite";
	argv[1] = (char*)"-create";
	argv[2] = (char*)"-s";
	argv[3] = (char*)fileName.c_str();
	argv[4] = (char*)"100";
	argv[5] = (char*)"42";


	
	m_testNum++;
	printTestMessage(m_testNum, "Testing for Number Driver \"./prog -create -s " + fileName + " " + std::to_string(AMOUNT) + " " + std::to_string(VALUE) + "\". Driver output below\n");
	
	NumberFileDriver::run(argc, argv);

	if(isFileAccessible(fileName))
	{
		file.open(fileName);

		file >> fileAmount;
		while(!file.eof())
		{
			file >> temp;
			nums.push_back(temp);
			if(temp != VALUE)	
			{
				isPassed = false;
				std::cerr << "ERROR: " << temp << " read in, expecting " << VALUE << std::endl;	
			}
		}


		if(fileAmount != nums.size())
		{
			std::cerr << "ERROR: " << fileAmount << " value excepted in file, " 
					<< nums.size() << " read. Is there a newline after last number?" << std::endl;
			isPassed = false;
		}
	}
	else
	{
		std::cerr << "ERROR: " << fileName << " not accessible!" << std::endl;
	}

	printPassFail(isPassed);

	file.close();
	return (isPassed);
}

bool Test::test_SortDriver1()
{
	bool isPassed = true;

	std::string inFileName = "test_random.dat";
	std::string outFileName = "test_random.out";
	std::ifstream inFile;
	std::ifstream outFile;
	const int argc = 5;

	const int AMOUNT = 1000;
	const int LOW = 0;
	const int HIGH = 5000;

	std::string sortName="";
	int sortAmount = 0;
	double sortTime = 0.0;

	char* argv[argc];
	argv[0] = (char*)"./SortingSuite";
	argv[1] = (char*)"-sort";
	argv[2] = (char*)"-bubble";
	argv[3] = (char*)inFileName.c_str();
	argv[4] = (char*)outFileName.c_str();
	
	m_testNum++;
	printTestMessage(m_testNum, "Testing for Sort Driver \"./prog -sort -bubble " + inFileName + " " + outFileName + "\" Driver output below\n");
	
	NumberFileGenerator::random(inFileName, AMOUNT, LOW, HIGH);
	SortDriver::run(argc, argv);
	outFile.open(outFileName);

	if(isFileAccessible(outFileName))
	{
		outFile >> sortName >> sortAmount >> sortTime;

		if(sortName != "bubble" || sortAmount != AMOUNT || !(sortTime > 0.0 && sortTime < 10.0))
		{
			std::cerr << "ERROR: read in the following from file: " << sortName << " " << sortAmount << " " << sortTime << std::endl;
			std::cerr << "Excpected: bubble " << AMOUNT << " and a time between 0.0 and 10.0" << std::endl;
			isPassed = false;
		}
	}
	else
	{
		std::cerr << "ERROR: " << outFileName << " not accessible!" << std::endl;
		isPassed = false;
	}

	printPassFail(isPassed);

	outFile.close();
	inFile.close();
	return (isPassed);
}

bool Test::test_SortDriver2()
{
	bool isPassed = true;

	std::string inFileName = "test_random.dat";
	std::string outFileName = "test_random.out";
	std::ifstream inFile;
	std::ifstream outFile;
	const int argc = 5;

	const int AMOUNT = 1000;
	const int LOW = 0;
	const int HIGH = 5000;

	std::string sortName="";
	int sortAmount = 0;
	double sortTime = 0.0;

	char* argv[argc];
	argv[0] = (char*)"./SortingSuite";
	argv[1] = (char*)"-sort";
	argv[2] = (char*)"-selection";
	argv[3] = (char*)inFileName.c_str();
	argv[4] = (char*)outFileName.c_str();
	
	m_testNum++;
	printTestMessage(m_testNum, "Testing for Sort Driver \"./prog -sort -selection " + inFileName + " " + outFileName + "\" Driver output below\n");
	
	NumberFileGenerator::random(inFileName, AMOUNT, LOW, HIGH);
	SortDriver::run(argc, argv);
	outFile.open(outFileName);

	if(isFileAccessible(outFileName))
	{
		outFile >> sortName >> sortAmount >> sortTime;

		if(sortName != "selection" || sortAmount != AMOUNT || !(sortTime > 0.0 && sortTime < 10.0))
		{
			std::cerr << "ERROR: read in the following from file: " << sortName << " " << sortAmount << " " << sortTime << std::endl;
			std::cerr << "Excpected: selection " << AMOUNT << " and a time between 0.0 and 10.0" << std::endl;
			isPassed = false;
		}
	}
	else
	{
		std::cerr << "ERROR: " << outFileName << " not accessible!" << std::endl;
		isPassed = false;
	}

	printPassFail(isPassed);

	outFile.close();
	inFile.close();
	return (isPassed);
}

bool Test::test_SortDriver3()
{
	bool isPassed = true;

	std::string inFileName = "test_random.dat";
	std::string outFileName = "test_random.out";
	std::ifstream inFile;
	std::ifstream outFile;
	const int argc = 5;

	const int AMOUNT = 1000;
	const int LOW = 0;
	const int HIGH = 5000;

	std::string sortName="";
	int sortAmount = 0;
	double sortTime = 0.0;

	char* argv[argc];
	argv[0] = (char*)"./SortingSuite";
	argv[1] = (char*)"-sort";
	argv[2] = (char*)"-insertion";
	argv[3] = (char*)inFileName.c_str();
	argv[4] = (char*)outFileName.c_str();
	
	m_testNum++;
	printTestMessage(m_testNum, "Testing for Sort Driver \"./prog -sort -insertion " + inFileName + " " + outFileName + "\" Driver output below\n");
	
	NumberFileGenerator::random(inFileName, AMOUNT, LOW, HIGH);
	SortDriver::run(argc, argv);
	outFile.open(outFileName);

	if(isFileAccessible(outFileName))
	{
		outFile >> sortName >> sortAmount >> sortTime;

		if(sortName != "insertion" || sortAmount != AMOUNT || !(sortTime > 0.0 && sortTime < 10.0))
		{
			std::cerr << "ERROR: read in the following from file: " << sortName << " " << sortAmount << " " << sortTime << std::endl;
			std::cerr << "Excpected: insertion " << AMOUNT << " and a time between 0.0 and 10.0" << std::endl;
			isPassed = false;
		}
	}
	else
	{
		std::cerr << "ERROR: " << outFileName << " not accessible!" << std::endl;
		isPassed = false;
	}

	printPassFail(isPassed);

	outFile.close();
	inFile.close();
	return (isPassed);
}

bool Test::test_SortDriver4()
{
	bool isPassed = true;

	std::string inFileName = "test_random.dat";
	std::string outFileName = "test_random.out";
	std::ifstream inFile;
	std::ifstream outFile;
	const int argc = 5;

	const int AMOUNT = 1000;
	const int LOW = 0;
	const int HIGH = 5000;

	std::string sortName="";
	int sortAmount = 0;
	double sortTime = 0.0;

	char* argv[argc];
	argv[0] = (char*)"./SortingSuite";
	argv[1] = (char*)"-sort";
	argv[2] = (char*)"-merge";
	argv[3] = (char*)inFileName.c_str();
	argv[4] = (char*)outFileName.c_str();
	
	m_testNum++;
	printTestMessage(m_testNum, "Testing for Sort Driver \"./prog -sort -merge " + inFileName + " " + outFileName + "\" Driver output below\n");
	
	NumberFileGenerator::random(inFileName, AMOUNT, LOW, HIGH);
	SortDriver::run(argc, argv);
	outFile.open(outFileName);

	if(isFileAccessible(outFileName))
	{
		outFile >> sortName >> sortAmount >> sortTime;

		if(sortName != "merge" || sortAmount != AMOUNT || !(sortTime > 0.0 && sortTime < 10.0))
		{
			std::cerr << "ERROR: read in the following from file: " << sortName << " " << sortAmount << " " << sortTime << std::endl;
			std::cerr << "Excpected: merge " << AMOUNT << " and a time between 0.0 and 10.0" << std::endl;
			isPassed = false;
		}
	}
	else
	{
		std::cerr << "ERROR: " << outFileName << " not accessible!" << std::endl;
		isPassed = false;
	}

	printPassFail(isPassed);

	outFile.close();
	inFile.close();
	return (isPassed);
}

bool Test::test_SortDriver5()
{
	bool isPassed = true;

	std::string inFileName = "test_random.dat";
	std::string outFileName = "test_random.out";
	std::ifstream inFile;
	std::ifstream outFile;
	const int argc = 5;

	const int AMOUNT = 1000;
	const int LOW = 0;
	const int HIGH = 5000;

	std::string sortName="";
	int sortAmount = 0;
	double sortTime = 0.0;

	char* argv[argc];
	argv[0] = (char*)"./SortingSuite";
	argv[1] = (char*)"-sort";
	argv[2] = (char*)"-quick";
	argv[3] = (char*)inFileName.c_str();
	argv[4] = (char*)outFileName.c_str();
	
	m_testNum++;
	printTestMessage(m_testNum, "Testing for Sort Driver \"./prog -sort -quick " + inFileName + " " + outFileName + "\" Driver output below\n");
	
	NumberFileGenerator::random(inFileName, AMOUNT, LOW, HIGH);
	SortDriver::run(argc, argv);
	outFile.open(outFileName);

	if(isFileAccessible(outFileName))
	{
		outFile >> sortName >> sortAmount >> sortTime;

		if(sortName != "quick" || sortAmount != AMOUNT || !(sortTime > 0.0 && sortTime < 10.0))
		{
			std::cerr << "ERROR: read in the following from file: " << sortName << " " << sortAmount << " " << sortTime << std::endl;
			std::cerr << "Excpected: quick " << AMOUNT << " and a time between 0.0 and 10.0" << std::endl;
			isPassed = false;
		}
	}
	else
	{
		std::cerr << "ERROR: " << outFileName << " not accessible!" << std::endl;
		isPassed = false;
	}

	printPassFail(isPassed);

	outFile.close();
	inFile.close();
	return (isPassed);
}

bool Test::test_SortDriver6()
{
	bool isPassed = true;

	std::string inFileName = "test_random.dat";
	std::string outFileName = "test_random.out";
	std::ifstream inFile;
	std::ifstream outFile;
	const int argc = 5;

	const int AMOUNT = 1000;
	const int LOW = 0;
	const int HIGH = 5000;

	std::string sortName="";
	int sortAmount = 0;
	double sortTime = 0.0;

	char* argv[argc];
	argv[0] = (char*)"./SortingSuite";
	argv[1] = (char*)"-sort";
	argv[2] = (char*)"-quick3";
	argv[3] = (char*)inFileName.c_str();
	argv[4] = (char*)outFileName.c_str();
	
	m_testNum++;
	printTestMessage(m_testNum, "Testing for Sort Driver \"./prog -sort -quick3 " + inFileName + " " + outFileName + "\" Driver output below\n");
	
	NumberFileGenerator::random(inFileName, AMOUNT, LOW, HIGH);
	SortDriver::run(argc, argv);
	outFile.open(outFileName);

	if(isFileAccessible(outFileName))
	{
		outFile >> sortName >> sortAmount >> sortTime;

		if(sortName != "quick3" || sortAmount != AMOUNT || !(sortTime > 0.0 && sortTime < 10.0))
		{
			std::cerr << "ERROR: read in the following from file: " << sortName << " " << sortAmount << " " << sortTime << std::endl;
			std::cerr << "Excpected: quick3 " << AMOUNT << " and a time between 0.0 and 10.0" << std::endl;
			isPassed = false;
		}
	}
	else
	{
		std::cerr << "ERROR: " << outFileName << " not accessible!" << std::endl;
		isPassed = false;
	}

	printPassFail(isPassed);

	outFile.close();
	inFile.close();
	return (isPassed);
}
