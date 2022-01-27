#include <iostream>
#include <string>

int main()
{	
	std::string word = "dogs";
	
	//Stack allocated array of strings:
	const int SIZE = 4;
	std::string words[SIZE];
	
	for(int i=0; i<SIZE; i++)
	{
		words[i] = "hi";
	}
	
	
	std::string* heapWords = nullptr;
	int size = 4;
	heapWords = new std::string[size];
	int lastIndex = 0;
	
	for(int i=0; i<size; i++)
	{
		heapWords[i] = "bye";
	}
	
	heapWords[3] = "wertyuiop";
	
	//Goal: print the last letter in every word
	//of the heap allocated array
	for(int i=0; i<size; i++)
	{
			lastIndex = heapWords[i].length()-1;
			std::cout << heapWords[i].at(lastIndex) << '\n';
	}
	return(0);
}