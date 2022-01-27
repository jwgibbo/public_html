/*
Notes for the 2020.04.07 lecture

Topic: Complexity
*/


//This will always run 10 times
for(int i=0; i<10; i++)
{
	//do something
}


//This will run n times
//n now controls the number of 
//instructions executed
for(int i=0; i<n; i++)
{
	//do something
}

for(int i=0; i<n; i++)
{
	for(int j=0; j<n; j++)
	{
		//do something
		//recall that this something
		//runs (i * j) times
	}
}

//All iterative sorts were nest loops
//abbreviated version of bubble sort
for(int i=0; i<n-1; i++)
{
	for(int j=0; j<n-1; j++)
	{
		//swap neighbors if needed
	}
}

//memory complexity

//constant space complexity
int x=0;
double dub=0.0;


//linear space complexity
std::cin >> size;
ptr = new int[size]; //amount of memory	needed	
					 //is  controlled by size,
					 //size is our n
					
//printing list using getEntry
for(int i=1; i<=myList.getLength(); i++)
{
	std::cout << myList.getEntry(i) << "\n";
}
