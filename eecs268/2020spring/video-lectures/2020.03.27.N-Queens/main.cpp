#include <iostream>

void recFunc(int i)
{
	if( i < 5 )
	{
		recFunc(i+1);
		std::cout << i << '\n';
	}
}

double recSum(double arr[], int size)
{
	//what is the base case?
	if( size <= 0 )
	{
		return( 0 );
	}
	else
	{
		//how can I make the problem slightly 
		//smaller and give the rest of the problem	
		//to the recursive call
		return(arr[size-1] + recSum(arr,size-1));
	}
}

bool isPalindrome(char arr[], int size)
{
	//if it's a palindrome due
	//to it's size, return true
	if(size <= 1)
	{
		return(true);
	}
	else
	{
		//do the first and last 
		//elements match?
		if(arr[0] != arr[size-1])
		{
			return(false);
		}
		else
		{
			return( isPalindrome((arr+1), size-2));
		}
	}
}

//  RACCAR

int main()
{
	char seq[] = {'a', 'b', 'a'}; //inital at declaration
	const int SIZE = 5;
	double* arr = new double[SIZE];
	double*  arrOffset = (arr+3);

	//recFunc(0);
	
	
	std::cout << "[ ";
	for(int i=0; i<SIZE; i++)
	{
		arr[i] = (i+1)*10.0;
		std:: cout << arr[i] << ' ';
	}
	std::cout << "]\n";
	
	std::cout << "arrOffset[0]=>" << arrOffset[0];
	std::cout << std::endl;
	
	return(0);
}